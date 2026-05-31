import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


# DOCUMENT FOLDER
DATA_PATH = "uploads"


# STORE DOCUMENTS
documents = []


# READ PDFs
for file in os.listdir(DATA_PATH):

    if file.endswith(".pdf"):

        path = os.path.join(DATA_PATH, file)

        loader = PyPDFLoader(path)

        documents.extend(loader.load())


# SPLIT TEXT
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = text_splitter.split_documents(documents)


# CREATE EMBEDDINGS
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# CREATE VECTOR DATABASE
vectorstore = FAISS.from_documents(
    docs,
    embeddings
)


# SAVE DATABASE
vectorstore.save_local("vectorstore")


print("Documents Ingested Successfully")