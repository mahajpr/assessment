from groq import Groq
history=[]
client = Groq(api_key="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")
def apicall(history,input1):
    response=client.chat.completions.create(
        temperature=0.1,
        max_tokens=50,
        model="llama-3.3-70b-versatile",
        messages=[{"role":"system","content":f"{history}"},
        {"role":"user","content":f"{input1}"}
        ]
)
    print(response.choices[0].message.content)
    return response.choices[0].message.content
for i in range(3):
    input1=input("enter your question")
    output=apicall(history,input1)
    history.append(output)
    print("output:",output)
