from openai import OpenAI
import os

client = OpenAI()

api_key = os.getenv("OPENAI_API_KEY")

def openai_chatbot():
    conversation = []
    system_prompt = {
        "role":"system", 
        "content":" You are a helpfull assistant. Please respond to the user queries"}
    conversation.append(system_prompt)
    while True:
        query = input("User: ")
        if query.lower() == "quit":
            print("Bot: Goodbye!! Have a Nice day")
            break
        conversation.append({"role":"user", "content": query})
        llm = client.chat.completions.create(
            model="gpt-4.1",
            messages=conversation
        )
        chat_response = llm.choices[0].message.content
        print(f"Bot: {chat_response}")
        conversation.append({"role":"assistant", "content":chat_response})

if __name__ == "__main__":
  print("Start chatting with the Bot (type 'quit' to stop)!")
  openai_chatbot()