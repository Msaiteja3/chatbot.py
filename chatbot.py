import spacy

# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")

def chatbot_response(user_input):
    """Generate a chatbot response based on user input."""
    # Process user input with spaCy
    doc = nlp(user_input.lower())

    # Analyze intent and keywords
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a program, but I'm doing great! How about you?"
    elif "your name" in user_input:
        return "I'm ChatGPT, your friendly chatbot!"
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day!"
    elif "weather" in user_input:
        return "I'm not equipped to check the weather right now, but it's always a good idea to carry an umbrella just in case!"
    elif "time" in user_input:
        return "I can't check the time right now, but clocks are everywhere these days!"
    else:
        return "I'm sorry, I didn't quite understand that. Can you rephrase?"

def chatbot():
    """Main chatbot loop."""
    print("Chatbot: Hello! I'm here to chat with you. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower():
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
