from langchain_community.document_loaders import PyPDFDirectoryLoader

def load_documents():

    loader = PyPDFDirectoryLoader("../knowledge_base")

    documents = loader.load()

    return documents