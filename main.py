from stt import record_audio, speech_to_text
from llm import ask_llm
from tts import speak
from speech_cleaner import clean_for_speech
from memory import add_user_message

STOP_WORDS = ["stop", "exit", "quit", "goodbye", "bye"]

def run_agent():
    print("🤖 Voice agent started. Say 'stop' to exit.\n")

    while True:
        record_audio()
        text = speech_to_text()
        print("📝 You said:", text)

        if any(word in text.lower() for word in STOP_WORDS):
            speak("Okay. Goodbye!")
            break

        add_user_message(text)

        response = ask_llm()
        spoken = clean_for_speech(response)

        print("🤖 Agent:", spoken)
        speak(spoken)

if __name__ == "__main__":
    run_agent()
