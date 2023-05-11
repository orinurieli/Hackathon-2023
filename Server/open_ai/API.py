import openai

openai.api_key = "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"

# Use OpenAI API to generate questions from the processed text
def summarize_text(text):
    model_engine = "text-davinci-002"
    prompt = f"Please summarize the following text:\n{text}\n\nSummary:"
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