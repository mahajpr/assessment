from groq import Groq
client = Groq(api_key="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")
response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role":"system","content":"i is sick"},
            {"role":"user","content":"i am sick"},
            {"role":"system","content":"check the grammer correction"},
            {"role":"user","content":"there a cow the valley"}
        ]
)
print(response.choices[0].message.content)