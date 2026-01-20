from groq import Groq
from dotenv import load_dotenv
import os
from memory import get_history, add_assistant_message

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_llm():
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=get_history()
    )
    answer = response.choices[0].message.content
    add_assistant_message(answer)
    return answer
