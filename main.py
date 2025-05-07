import requests

# Groq-compatible OpenAI endpoint
url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": "Bearer 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",
    "Content-Type": "application/json"
}

print("Welcome to the AI assistant. Type your question below.")
print("Type 'exit' to end the conversation.\n")

while True:
    user_question = input("You: ")

    if user_question.strip().lower() == "exit":
        print("Goodbye!")
        break

    data = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that will answer with simple and short answers"},
            {"role": "user", "content": user_question}
        ],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        print("Assistant:", result["choices"][0]["message"]["content"], "\n")
    else:
        print(f"Error: {response.status_code} - {response.text}\n")
