import openai

openai.api_key = ""

# Use OpenAI API to generate questions from the processed text
def summarize_text(text):
    model_engine = "text-davinci-002"
    prompt = f"Please summarize the following text in and find the main problem," \
             f" :\n{text}\n\n" \
             f"see if there is similarity to past summary of a problem" \
             f" from the following summaries that matches and if there is, use it as the response :\n{text}\n\n/" \
             f"Summary:"
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
