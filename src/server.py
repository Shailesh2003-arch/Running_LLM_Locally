from fastapi import FastAPI, Body
from ollama import Client

# Initiating the server instance from FastAPI.
app = FastAPI()


# creating a client which will chat to our backend.
client = Client(
    host="http://localhost:11434"
)

@app.get('/')
def index():
    return {
        'data':'hello from the server 🚀'
    }

@app.post('/chat')
def chat(message:str= Body(...,description="The message")):
    response = client.chat(
        # you have to pass the model here that you've downloaded.
        model='qwen3:1.7b',
        messages=[
            {'role':'user', 'content':message}
        ]
    )
    return {"response": response.message.content}