from groq import Groq
client = Groq(api_key="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")
response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role":"system","content":"In the generated answer the word limit should be 200, It should be friendly manner, the wording should  be in paragraph and the output format will be in  json "},
        {"role":"user","content":"give the email for reminder of the policy holder"}
        ]
)
print(response.choices[0].message.content)