
import edge_tts
import asyncio

async def text_to_speech():
    text = input("📝 اكتبي النص الذي تريدين تحويله إلى صوت: ")

    output_file = "response.mp3"

    voice = "ar-SA-ZariyahNeural"

    communicate = edge_tts.Communicate(
        text,
        voice
    )

    await communicate.save(output_file)

    print("\n✅ تم تحويل النص إلى صوت بنجاح!")
    print("🔊 تم حفظ الملف باسم:", output_file)

asyncio.run(text_to_speech())