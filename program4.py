from groq import Groq
client = Groq(api_key="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")
response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role":"system","content":"you are a helpful assistant that correct english grammer "},
            {"role":"user","content":"i is sick"},
            {"role":"assistant","content":"i am sick"},
            {"role":"user","content":"she go to school yesterday"},
            {"role":"assistant","content":"she went to school yesterday"},
            {"role":"user","content":"there a cow the valley"}
        ]
)

print(response.choices[0].message.content)
