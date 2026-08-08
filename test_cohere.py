import cohere

# ضع مفتاح Cohere API هنا
API_KEY = "cohere_hbQaBDdzk9wGMz0LGnP7AtYNCxrJEL4TnCONeZQy28XIUb"

co = cohere.ClientV2(api_key=API_KEY)

response = co.chat(
    model="command-a-plus-05-2026",
    messages=[
        {
            "role": "user",
            "content": "Hello, introduce yourself briefly."
        }
    ]
)

# استخراج النص فقط وتجاهل thinking
for item in response.message.content:
    if getattr(item, "type", None) == "text":
        print("🤖 Cohere:")
        print(item.text)
        break
