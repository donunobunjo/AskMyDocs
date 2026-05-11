# from langchain.embeddings import OllamaEmbeddings
from langchain_community.embeddings import OllamaEmbeddings

def get_embedding_function():
    return OllamaEmbeddings(
        model="nomic-embed-text"
    )
