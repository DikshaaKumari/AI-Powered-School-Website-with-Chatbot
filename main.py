from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

from chatbot import ask_chatbot


app = FastAPI()


# CORS

app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


# REQUEST MODEL

class ChatRequest(BaseModel):

    message:str


# HOME ROUTE

@app.get("/")

def home():

    return {

        "message":
        "RAG Chatbot Running"
    }


# CHAT ENDPOINT

@app.post("/chat")

def chat(request:ChatRequest):

    answer = ask_chatbot(request.message)

    return {

        "reply":answer
    }