import speech_recognition as sr
import cohere
import edge_tts
import asyncio
from playsound import playsound

# =========================
# Cohere API
# =========================

API_KEY = "YOUR_COHERE_API_KEY"

co = cohere.ClientV2(api_key=API_KEY)

# =========================
# Text-to-Speech
# =========================

async def text_to_speech(text):
    output_file = "response.mp3"
    voice = "en-US-AriaNeural"

    communicate = edge_tts.Communicate(
        text,
        voice
    )

    await communicate.save(output_file)


# =========================
# Voice Assistant
# =========================

recognizer = sr.Recognizer()

print("🎤 Voice-to-Voice AI Assistant")
print("================================")

with sr.Microphone() as source:

    print("🔊 Adjusting microphone...")
    recognizer.adjust_for_ambient_noise(source, duration=1)

    print("🎤 Speak now...")
    audio = recognizer.listen(source)


# =========================
# Speech-to-Text
# =========================

try:

    text = recognizer.recognize_google(
        audio,
        language="en-US"
    )

    print("\n👤 You:")
    print(text)


    # =========================
    # LLM - Cohere
    # =========================

    response = co.chat(
        model="command-a-plus-05-2026",
        messages=[
            {
                "role": "user",
                "content": text
            }
        ]
    )


    # =========================
    # Extract Cohere Response
    # =========================

    reply = ""

    for item in response.message.content:

        if getattr(item, "type", None) == "text":
            reply += item.text


    print("\n🤖 Cohere:")
    print(reply)


    # =========================
    # Text-to-Speech
    # =========================

    asyncio.run(text_to_speech(reply))

    print("\n🔊 Response converted to speech!")
    print("📁 Saved as: response.mp3")


    # =========================
    # Play Automatically
    # =========================

    playsound("response.mp3")


# =========================
# Errors
# =========================

except sr.UnknownValueError:

    print("❌ I could not understand the audio.")

except sr.RequestError as e:

    print("❌ Speech recognition service error:")
    print(e)

except Exception as e:

    print("❌ An error occurred:")
    print(e)
