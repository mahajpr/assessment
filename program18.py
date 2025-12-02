from groq import Groq
client = Groq(api_key="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")
prompt="are wild  life safe for humans or not?"
print("Cycle 0 (Original Prompt):")
print(prompt)
for i in range(1,4):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role":"system","content":"improve this given prompt"},
            {"role":"user","content":prompt}
        ]
        )
improved_prompt=response.choices[0].message.content
print("Cycle {i} (Improved Prompt):")
print(improved_prompt)
prompt=improved_prompt
