import os
import numpy as np
import faiss
import requests
from dotenv import load_dotenv

load_dotenv()

EMBED_URL = os.getenv("LM_EMBEDDINGS_URL", "http://localhost:1234/v1/embeddings")
EMBED_MODEL = os.getenv("LM_EMBED_MODEL", "nomic-embed-text-v1.5")
LLM_URL = os.getenv("LM_STUDIO_URL", "http://localhost:1234/v1/chat/completions")
LLM_MODEL = os.getenv("LM_MODEL", "hermes-3-llama-3.2-3b")

class RAGEngine:
    def __init__(self):
        self.index = None
        self.chunks = []          # lista de (texto, metadados)
        self.dimension = 768      # dimensão do embedding do Nomic

    def get_embedding(self, text):
        """Obtém embedding via LM Studio."""
        payload = {
            "model": EMBED_MODEL,
            "input": text
        }
        try:
            resp = requests.post(EMBED_URL, json=payload, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            return np.array(data["data"][0]["embedding"], dtype=np.float32)
        except Exception as e:
            print(f"Erro no embedding: {e}")
            return None

    def add_documents(self, chunks):
        """Indexa chunks no FAISS."""
        self.chunks = chunks
        embeddings = []
        for chunk in chunks:
            emb = self.get_embedding(chunk.page_content)
            if emb is None:
                raise Exception("Falha ao obter embedding")
            embeddings.append(emb)

        vectors = np.vstack(embeddings)
        self.index = faiss.IndexFlatL2(self.dimension)
        self.index.add(vectors)

    def retrieve(self, query, top_k=3):
        """Recupera os chunks mais relevantes para a pergunta."""
        if self.index is None:
            return []
        query_emb = self.get_embedding(query)
        if query_emb is None:
            return []
        distances, indices = self.index.search(query_emb.reshape(1, -1), top_k)
        results = []
        for i, idx in enumerate(indices[0]):
            if idx != -1:
                results.append({
                    "text": self.chunks[idx].page_content,
                    "score": distances[0][i],
                    "metadata": self.chunks[idx].metadata
                })
        return results

    def generate_answer(self, query, context_chunks):
        """Gera resposta usando Hermes 3."""
        context = "\n\n".join([chunk["text"] for chunk in context_chunks])
        prompt = f"""
Você é um assistente que responde perguntas com base no contexto fornecido. Use apenas o contexto para responder. Responda em português.

Contexto:
{context}

Pergunta: {query}

Resposta:
"""
        payload = {
            "model": LLM_MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.3,
            "max_tokens": 500
        }
        try:
            resp = requests.post(LLM_URL, json=payload)
            resp.raise_for_status()
            data = resp.json()
            return data["choices"][0]["message"]["content"].strip()
        except Exception as e:
            return f"Erro na geração: {e}"
        
        