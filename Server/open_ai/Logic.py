import API

if __name__ == "__main__":
    text = "This is a sample text that we want to summarize using OpenAI's GPT-3."
    summary = API.summarize_text(text)
    print(summary)

