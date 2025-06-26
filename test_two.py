from anthropic import Anthropic
import os


client = Anthropic()

api_key_anthropic = os.getenv("ANTHROPIC_API_KEY")

def anthropic_chatbot():
    conversations = []
    while True:
        user_query = input("User: ")
        if user_query.strip().lower() in ['bye', 'goodbye']:
            break
        conversations.append(
            {"role":"user", "content": user_query}
        )  
        llms= client.messages.create(
            model = "claude-3-7-sonnet-20250219",
            max_tokens = 200,
            #system = "You are a helpfull assistant. Please respond to the user queries",
            messages = conversations
            )
        chat_responses = llms.content[0].text
        print(f"Bot: {chat_responses}")
        conversations.append({"role":"assistant", "content":chat_responses})

if __name__ == "__main__":
  print("Start chatting with the Bot (type 'bye' or 'goodbye' to stop)!")
  anthropic_chatbot()