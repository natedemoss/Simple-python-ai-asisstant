import requests
from datetime import datetime

# Groq-compatible OpenAI endpoint
url = "https://api.groq.com/openai/v1/chat/completions"

# Replace with your actual key
headers = {
    "Authorization": "Bearer your-api-key",
    "Content-Type": "application/json"
}

log_file = "conversation_log.txt"

# Welcome message
print("Welcome to the AI assistant. Type your question below.")
print("Type 'exit' to end the conversation.\n")

# Start of conversation log
with open(log_file, "a", encoding="utf-8") as log:
    log.write(f"\n--- Conversation started at {datetime.now()} ---\n")

while True:
    user_question = input("You: ")

    if user_question.strip().lower() == "exit":
        print("Goodbye!")
        with open(log_file, "a", encoding="utf-8") as log:
            log.write("--- Conversation ended ---\n")
        break

    data = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": user_question}
        ],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        assistant_reply = result["choices"][0]["message"]["content"].strip()
        print("Assistant:", assistant_reply, "\n")

        # Log to file
        with open(log_file, "a", encoding="utf-8") as log:
            log.write(f"You: {user_question}\n")
            log.write(f"Assistant: {assistant_reply}\n\n")

    else:
        error_msg = f"Error: {response.status_code} - {response.text}"
        print(error_msg + "\n")
        with open(log_file, "a", encoding="utf-8") as log:
            log.write(error_msg + "\n\n")
