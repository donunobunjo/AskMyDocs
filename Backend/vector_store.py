# from langchain.vectorstores import Chroma
from langchain_community.vectorstores import Chroma
from embeddings import get_embedding_function

CHROMA_PATH = "chroma_db"

def get_vector_store():
    embedding = get_embedding_function()
    
    return Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embedding
    )
