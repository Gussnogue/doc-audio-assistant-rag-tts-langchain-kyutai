import os
import tempfile
import tiktoken
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, TextLoader

def load_document(file):
    """Carrega documento a partir do arquivo enviado (PDF ou TXT)."""
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.name)[1]) as tmp:
        tmp.write(file.getvalue())
        tmp_path = tmp.name

    try:
        if file.type == "application/pdf":
            loader = PyPDFLoader(tmp_path)
        else:
            loader = TextLoader(tmp_path, encoding="utf-8")
        docs = loader.load()
    finally:
        os.unlink(tmp_path)

    return docs

def chunk_document(docs, chunk_size=500, chunk_overlap=50):
    """Divide documentos em chunks."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""],
        length_function=len,
    )
    chunks = text_splitter.split_documents(docs)
    return chunks

def count_tokens(text, model="gpt-3.5-turbo"):
    """Conta tokens usando tiktoken (útil para debug)."""
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

