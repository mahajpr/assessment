from groq import Groq
client = Groq(api_key="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")
response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role":"system" , "content":"do you want text,JSON or bullet points"}, 
            {"role":"user","content":"i should prefer bullet points about is the wild animals are safe?"}
        ]
)
print(response.choices[0].message.content)