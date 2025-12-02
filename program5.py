from groq import Groq
client = Groq(api_key="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")
puzzle="you bought 10 tennis balls.you give 5 tennis balls to your friend and another 2 tennis balls to your sister. how many tennis balls you have remaining"
response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role":"system","content":"while you answering a question always use this format"
                "Thought: explain your reasoning.\n"
                "Action: describe the calculation.\n"
                "Result: give the final answer.\n"},
                {"role":"user","content":f"solve this puzzle using thought,action and result format {puzzle}"}]
)
print(puzzle)
print(response.choices[0].message.content)
