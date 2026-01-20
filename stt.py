#Record Voice (Microphone → WAV)

import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(filename="audio/input.wav", duration=5, fs=44100):
    print("🎙️ Speak now...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, recording)
    print("✅ Recording saved")

#Speech → Text (Whisper)
import whisper

model = whisper.load_model("base")

def speech_to_text(audio_path="audio/input.wav"):
    result = model.transcribe(audio_path)
    return result["text"]
