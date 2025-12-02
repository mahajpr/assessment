
from groq import Groq
client = Groq(api_key="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")
response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role":"user","content":"give me a receipe of sandwich"}
        ]
)
with open("program.txt","r") as f:
    content=f.read()
print(content)
print(response.choices[0].message.content)
