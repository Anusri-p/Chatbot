import openai
import random

openai.api_key="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"

def chatbot(prompt):
    words = prompt.lower().split()
    
    # Simple dynamic responses based on keywords
    if any(word in words for word in ["hello", "hi", "hey"]):
        return random.choice(["Hello! How can I assist you?", "Hi there! What's on your mind?", "Hey! How can I help?"])
    elif any(word in words for word in ["how", "you"]):
        return random.choice(["I'm just a program, but I'm here to help you!", "I'm doing great, thanks for asking! How about you?"])
    elif any(word in words for word in ["role", "function", "purpose"]):
        return "My role is to assist you with your questions and provide useful information."
    elif any(word in words for word in ["bye", "exit", "quit"]):
        return "Goodbye! Have a wonderful day!"
    elif any(word in words for word in ["name"]):
        return "I am your friendly chatbot! What's your name?"
    elif "?" in prompt:
        return "That's an interesting question! Can you tell me more?"
    else:
        return "I'm here to help! Can you clarify or give me more details?"

   
if __name__ == "__main__":
    print("Chatbot: Hello! Ask me anything. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot(user_input)
        print("Chatbot:", response)