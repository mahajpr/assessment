from groq import Groq
client = Groq(api_key="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")
response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=1.0,
        messages=[{"role":"user","content":"write the 3 paragraphs about is the wild life is safe or not for humans "}],
        max_tokens=300
)
print(response.choices[0].message.content)