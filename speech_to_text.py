
import speech_recognition as sr

recognizer = sr.Recognizer()

print("🎤 Speech-to-Text Test")
print("======================")

with sr.Microphone() as source:

    print("🔊 جاري ضبط المايك...")
    recognizer.adjust_for_ambient_noise(source, duration=1)

    print("🎤 تكلمي الآن...")

    audio = recognizer.listen(source)

try:

    text = recognizer.recognize_google(
        audio,
        language="ar-SA"
    )

    print("\n📝 النص الذي تم التعرف عليه:")
    print(text)

except sr.UnknownValueError:

    print("❌ لم أستطع فهم الصوت.")

except sr.RequestError as e:

    print("❌ حدث خطأ في خدمة التعرف على الصوت:")
    print(e)