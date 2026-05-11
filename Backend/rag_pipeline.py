from langchain_text_splitters import RecursiveCharacterTextSplitter
from file_loader import load_pdf
from vector_store import get_vector_store
import ollama

def process_document(file_bytes, filename):
    documents = load_pdf(file_bytes)
    
    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    
    chunks = splitter.split_documents(documents)
    
    # Store in vector DB
    vector_store = get_vector_store()
    vector_store.add_documents(chunks)
    vector_store.persist()


def query_rag(query):
    vector_store = get_vector_store()
    
    # Retrieve relevant chunks
    docs = vector_store.similarity_search(query, k=3)
    
    context = "\n\n".join([doc.page_content for doc in docs])
    
    prompt = f"""
    Answer the question using ONLY the context below.
    
    Context:
    {context}
    
    Question:
    {query}
    """
    
    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response['message']['content']
