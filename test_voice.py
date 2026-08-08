import sounddevice as sd
import numpy as np
import wave
import speech_recognition as sr

SAMPLE_RATE = 16000
DURATION = 10
FILE_NAME = "voice.wav"

print("🎤 تكلمي الآن لمدة 5 ثواني...")

audio = sd.rec(
    int(DURATION * SAMPLE_RATE),
    samplerate=SAMPLE_RATE,
    channels=1,
    dtype="int16"
)

sd.wait()

with wave.open(FILE_NAME, "wb") as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(SAMPLE_RATE)
    wf.writeframes(audio.tobytes())

print("✅ تم تسجيل الصوت.")
print("📝 جاري تحويل الصوت إلى نص...")

recognizer = sr.Recognizer()

with sr.AudioFile(FILE_NAME) as source:
    recorded_audio = recognizer.record(source)

try:
    text = recognizer.recognize_google(
        recorded_audio,
        language="ar-SA"
    )

    print("✅ النص الذي فهمه النظام:")
    print(text)

except sr.UnknownValueError:
    print("❌ لم أستطع فهم الكلام.")

except sr.RequestError as e:
    print("❌ حصلت مشكلة في خدمة تحويل الصوت إلى نص:")
    print(e)
