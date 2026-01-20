import re

def clean_for_speech(text: str) -> str:
    # Remove markdown bold/italic
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"\*(.*?)\*", r"\1", text)

    # Remove numbered lists (1. 2. 3.)
    text = re.sub(r"\n?\s*\d+\.\s*", ". ", text)

    # Remove bullet points (- • *)
    text = re.sub(r"\n?\s*[-•]\s*", ". ", text)

    # Remove extra newlines
    text = re.sub(r"\n+", ". ", text)

    # Clean repeated punctuation
    text = re.sub(r"\.\s*\.", ".", text)

    return text.strip()
