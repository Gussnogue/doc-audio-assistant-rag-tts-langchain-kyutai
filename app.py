import streamlit as st
import os
from document_processor import load_document, chunk_document
from rag_engine import RAGEngine
from tts_generator import TTSGenerator
from utils import clear_temp_files

st.set_page_config(page_title="Narrador de Documentos", layout="wide")
st.title("🎧 Narrador de Documentos com RAG e Voz Sintetizada")
st.markdown("Faça upload de um documento, faça perguntas e ouça as respostas narradas.")

# Inicialização de estado
if "rag" not in st.session_state:
    st.session_state.rag = None
if "tts" not in st.session_state:
    st.session_state.tts = TTSGenerator()
if "processed" not in st.session_state:
    st.session_state.processed = False
if "temp_files" not in st.session_state:
    st.session_state.temp_files = []

# Sidebar para configurações de voz
with st.sidebar:
    st.header("Configurações de Voz")
    voice_name = st.selectbox(
        "Escolha uma voz:",
        ["alba", "marius", "javert", "jean", "fantine", "cosette", "eponine", "azelma"]
    )

# Upload de documento
uploaded_file = st.file_uploader("Carregue um documento (PDF ou TXT)", type=["pdf", "txt"])
if uploaded_file is not None:
    if not st.session_state.processed:
        with st.spinner("Processando documento..."):
            docs = load_document(uploaded_file)
            chunks = chunk_document(docs)
            st.write(f"Documento dividido em {len(chunks)} trechos.")

            # Inicializa RAG e indexa
            rag = RAGEngine()
            rag.add_documents(chunks)
            st.session_state.rag = rag
            st.session_state.processed = True
        st.success("Documento indexado com sucesso!")

# Se já houver documento processado, permite perguntas
if st.session_state.processed:
    query = st.text_input("Digite sua pergunta sobre o documento:")
    if query:
        with st.spinner("Buscando resposta..."):
            context = st.session_state.rag.retrieve(query, top_k=3)
            if not context:
                st.warning("Nenhum trecho relevante encontrado.")
            else:
                answer = st.session_state.rag.generate_answer(query, context)
                st.markdown("### 🤖 Resposta")
                st.write(answer)

                # Gerar áudio da resposta
                if st.button("🔊 Ouvir resposta"):
                    with st.spinner("Gerando áudio..."):
                        audio_path = st.session_state.tts.generate_from_text(
                            answer,
                            voice=voice_name,
                            voice_file=None
                        )
                        st.session_state.temp_files.append(audio_path)
                        st.audio(audio_path, format="audio/wav")

# Limpeza de arquivos temporários ao final
if st.button("Limpar arquivos temporários"):
    clear_temp_files(st.session_state.temp_files)
    st.session_state.temp_files = []
    st.success("Arquivos temporários removidos.")

    