rom groq import Groq
client = Groq(api_key="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")
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system","content": "Follow these conditions:\n"
                                     "Word limit: 200 words\n"
                                     "Tone: professional\n"
                                     "Style: paragraph writing\n"
                                     "Output format: JSON only\n"},
        {"role": "user","content": "Give an email reminder for the policy holder."}]
)
print(response.choices[0].message.content)
