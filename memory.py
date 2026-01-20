conversation_history = [
    {"role": "system", "content": "You are a helpful voice assistant. Respond in plain text, no markdown, no lists, no emojis."}
]

def add_user_message(text):
    conversation_history.append({"role": "user", "content": text})

def add_assistant_message(text):
    conversation_history.append({"role": "assistant", "content": text})

def get_history():
    return conversation_history
