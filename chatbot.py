from openai import OpenAI

from rag import search_docs


# DEEPSEEK CLIENT

client = OpenAI(

    api_key="sk-abbbd8ac0c004660ae28c615ee24e2b8",

    base_url="https://api.deepseek.com"
)


# MAIN CHATBOT FUNCTION

def ask_chatbot(question):

    # SEARCH DOCUMENTS

    docs = search_docs(question)


    # CREATE CONTEXT

    context = "\n".join(

        [doc.page_content for doc in docs]
    )


    # PROMPT

    prompt = f"""

    You are a school assistant chatbot.

    Answer ONLY from the given context.

    If answer is unavailable,
    say:
    "Information not found in documents."

    Context:
    {context}

    Question:
    {question}

    """


    # DEEPSEEK RESPONSE

    response = client.chat.completions.create(

        model="deepseek-chat",

        messages=[

            {
                "role":"system",

                "content":
                "You are a helpful school chatbot."
            },

            {
                "role":"user",

                "content":prompt
            }
        ],

        temperature=0.3
    )


    return response.choices[0].message.content