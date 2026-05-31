from langchain_community.vectorstores import FAISS

from langchain_community.embeddings import HuggingFaceEmbeddings


# LOAD EMBEDDINGS

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# LOAD VECTOR DATABASE

vectorstore = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)


# SEARCH FUNCTION

def search_docs(query):

    docs = vectorstore.similarity_search(
        query,
        k=3
    )

    return docs