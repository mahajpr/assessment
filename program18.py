from groq import Groq
client = Groq(api_key="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")
response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            # # {"role":"system","content":"are wild  life safe for humans or not?"},
            # {"role":"system" , "content":"Are wild animals a threat to human safety, and what precautions can be taken to minimize the risk of encounters gone wrong?"}, 
            {"role":"system","content":"In areas where humans and wildlife interact, what are the best practices for preventing conflicts and ensuring human safety, while also respecting and conserving wildlife populations?"},
            {"role":"user","content":"improve this given prompt"}
        ]
)
print(response.choices[0].message.content)