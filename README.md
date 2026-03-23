# 🎧 Doc Audio Assistant: RAG + TTS Local com LangChain, Hermes 3 e Pocket TTS

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white)](https://www.langchain.com/)
[![FAISS](https://img.shields.io/badge/FAISS-005A9C?style=flat-square&logo=meta&logoColor=white)](https://github.com/facebookresearch/faiss)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![LM Studio](https://img.shields.io/badge/LM_Studio-0A0A0A?style=flat-square&logo=ai&logoColor=white)](https://lmstudio.ai/)
[![Pocket TTS](https://img.shields.io/badge/Pocket_TTS-FF6B6B?style=flat-square)](https://kyutai.org/tts)

> Assistente documental que combina **RAG local** (LangChain + FAISS + Nomic Embed), **LLM local** (Hermes 3 via LM Studio) e **TTS local** (Pocket TTS). Upload de PDF/TXT, perguntas em português e respostas narradas com vozes éticas. Totalmente offline, privado e integrado em Streamlit.

---

## 🛠️ Stack Principal

| **Linguagem** | **RAG & Indexação** | **IA Local** | **TTS** | **Interface** |
|---------------|---------------------|--------------|---------|---------------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) | ![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square) ![FAISS](https://img.shields.io/badge/FAISS-005A9C?style=flat-square) | ![LM Studio](https://img.shields.io/badge/LM_Studio-0A0A0A?style=flat-square) ![Hermes 3](https://img.shields.io/badge/Hermes_3-3B-FFD700?style=flat-square) | ![Pocket TTS](https://img.shields.io/badge/Pocket_TTS-FF6B6B?style=flat-square) | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square) |

---

## ✨ Funcionalidades

- 📄 **Upload de documentos**: PDF ou TXT.
- 🔍 **Processamento RAG**: divisão em chunks, embeddings locais com Nomic, indexação FAISS.
- 🤖 **Respostas com IA**: geração de respostas com Hermes 3 (LM Studio).
- 🔊 **Síntese de fala**: Pocket TTS com vozes éticas pré‑definidas (não há clonagem para evitar questões de consentimento).
- 🖥️ **Interface completa**: Streamlit com layout amigável.

---

## 🧠 Componentes Técnicos

### 1. RAG (Retrieval-Augmented Generation)
- **LangChain**: orquestração da pipeline de documentos.
- **Nomic Embed**: embeddings via LM Studio (porta 1234).
- **FAISS**: busca vetorial rápida e local.

### 2. Geração de Respostas
- **Hermes 3** (3B) rodando no LM Studio, inferência local, zero dados na nuvem.

### 3. Text-to-Speech
- **Kyutai Pocket TTS** modelo de 100M parâmetros que roda em CPU, com vozes de alta qualidade e latência baixa.

---

## 🚀 Como Executar

### Pré‑requisitos
- Python 3.9+
- **LM Studio** com os modelos:
  - `hermes-3-llama-3.2-3b`
  - `nomic-embed-text-v1.5`
  (servidor ativo na porta 1234)

### Passo a passo

1. **Clone o repositório**
   ```bash
   git clone https://github.com/Gussnogue/doc-audio-assistant-rag-tts-langchain-kyutai.git
   cd doc-audio-assistant-rag-tts-langchain-kyutai

2. **Crie e ative um ambiente virtual**
   ```bash
   python -m venv venv
   venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```
3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação**
   ```bash
   streamlit run app.py
   ```

# 📁 Estrutura de Pastas
```bash
doc-audio-assistant-rag-tts-langchain-kyutai/
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
├── app.py
├── document_processor.py      # carregamento e chunking
├── rag_engine.py              # embeddings, FAISS, geração
├── tts_generator.py           # Pocket TTS (vozes éticas)
└── utils.py                   # utilitários
```

# 🧪 Exemplo de Uso

- **Faça upload de um PDF (ex: artigo científico, relatório).**

- **Digite uma pergunta em português, como: "Qual é a principal contribuição deste trabalho?"**

- **O sistema busca os trechos relevantes, gera uma resposta e exibe na tela.**

- **Clique em 🔊 Ouvir resposta – o áudio é sintetizado com a voz escolhida.**

# 🙌 Créditos e Agradecimentos

Este projeto utiliza tecnologias incríveis da comunidade open‑source:

- Kyutai: pelo desenvolvimento do Pocket TTS e pelo compromisso com a ciência aberta.

- LM Studio: por permitir rodar LLMs localmente com facilidade.

- LangChain: pela abstração robusta de pipelines RAG.

- FAISS: pela indexação vetorial ultra‑rápida.

🔗 Conheça mais sobre o trabalho do Kyutai em kyutai.org.

# 📄 Licença

MIT License – sinta‑se à vontade para usar, modificar e distribuir.
