from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from rag_pipeline import process_document, query_rag

app = FastAPI()

# Allow React frontend to communicate
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store session state (simple version)
DOCUMENT_READY = False
#######
@app.get("/")
async def root():
    return {
        "status": "Backend is running",
        "message": "RAG API working successfully"
    }

##########3


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    global DOCUMENT_READY
    
    contents = await file.read()
    
    # Process document into vector DB
    process_document(contents, file.filename)
    
    DOCUMENT_READY = True
    
    return {"message": "Document processed successfully"}

@app.post("/chat/")
async def chat(query: str):
    if not DOCUMENT_READY:
        return {"error": "Upload a document first"}
    
    answer = query_rag(query)
    
    return {"response": answer}