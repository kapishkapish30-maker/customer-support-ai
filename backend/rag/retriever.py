from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from rag.loader import load_documents
from rag.embeddings import get_embeddings

db = None

def initialize_vectorstore():
    global db

    documents = load_documents()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    embeddings = get_embeddings()

    db = FAISS.from_documents(
        chunks,
        embeddings
    )

def retrieve(query):

    docs = db.similarity_search(query, k=3)

    context=""

    for doc in docs:
        context += doc.page_content + "\n"

    return context