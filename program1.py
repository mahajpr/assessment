from groq import Groq
client = Groq(api_key="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")
with open("program.txt","r") as f:
    content=f.read()
    topic = "sandwich recipe"
    tone = "friendly"
    final_prompt = content.format(topic=topic, tone=tone)
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role":"user","content":final_prompt}
        ]
)
print(content)
print(final_prompt)
print(response.choices[0].message.content)


