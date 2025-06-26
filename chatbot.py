from openai import OpenAI
from anthropic import Anthropic
import os

openai_client = OpenAI()
anthropic_client = Anthropic()

api_key_openai = os.getenv("OPENAI_API_KEY")
api_key_anthropic = os.getenv("ANTHROPIC_API_KEY")

conversation = []

def openai_chatbot(user_query):
        system_prompt = [{
        "role":"system", 
        "content":" You are a helpfull assistant. Please respond to the user queries"}]
        conversation.append({"role":"user", "content": user_query})
        llm = openai_client.chat.completions.create(
            model="gpt-4.1",
            messages=system_prompt+conversation
        )
        chat_response = llm.choices[0].message.content
        print(f"OpenAI: {chat_response}")
        conversation.append({"role":"assistant", "content":chat_response})
        return
    

def anthropic_chatbot(user_query):
    conversation.append({"role":"user", "content":user_query})
    llm = anthropic_client.messages.create(
        model = "claude-3-7-sonnet-20250219",
        max_tokens = 200,
        #system = "You are a helpfull assistant. Please respond to the user queries",
        messages = conversation
        )
    chat_response = llm.content[0].text.strip()
    print(f"Anthropic: {chat_response}")
    conversation.append({"role":"assistant", "content":chat_response})
    return
    
def chatbot():
    while True:
        user_query = input("You: ")
        if user_query.strip().lower() in ['exit', 'bye','goodbye', 'thank you']:
            openai_exit = openai_chatbot("Say goodbye to the user in a friendly manner")
            anthropic_exit = anthropic_chatbot("Say Goodbye to the user in a friendly manner")
            break
        openai_reply = openai_chatbot(user_query)
        anthropic_reply = anthropic_chatbot(user_query)

def main():
    print("Welcome to the chatbot! Type 'exit' to end the conversation")
    chatbot()

if __name__ == "__main__":
    main()