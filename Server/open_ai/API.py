import openai

openai.api_key = ""

# Use OpenAI API to generate questions from the processed text
def summarize_text(text):
    model_engine = "text-davinci-002"
    prompt = text
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=3500,
        n=1,
        stop=None,
        temperature=0.3,
    )
    message = completions.choices[0].text.strip()
    return message

'''
I am going to send you a history of a calls center that were resolved in "json" format.
    {
        "problem": "The internet is slow",
        "solution": "Power reset your modem/router",
        "ranked": 6
    },
    {
        "problem": "The internet connection appears as Failed",
        "solution": "Power reset your modem/router",
        "ranked": 8
    },
    {
        "problem": "Network connection stuck",
        "solution": "Replace modem/router",
        "ranked": 7
    }
I need your help to resolve another issue based on the previous data.
Add short suggestions by your experience in new field. The solution fields must base on the data above.
before your solution, summarize the issue and give a short solution in the above template.
do not rank your solution.
do not add extra fields except the suggestion field.

the issue:
"Hi, my name is Maria. In the last 3 hours, my internet is failed and is back many times."
'''