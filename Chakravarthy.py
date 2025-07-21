import random

def get_response(user_input):
    user_input = user_input.lower()

    greetings = ["hello", "hi", "hey", "good morning", "good evening"]
    sad_words = ["sad", "depressed", "unhappy", "down", "miserable"]
    anxiety_words = ["anxious", "stressed", "worried", "nervous"]
    lonely_words = ["lonely", "alone", "isolated"]
    thanks_words = ["thank you", "thanks", "thx"]

    if any(word in user_input for word in greetings):
        return random.choice([
            "Hi there! How are you feeling today?",
            "Hello! I'm here for you. How’s your day going?"
        ])

    elif any(word in user_input for word in sad_words):
        return random.choice([
            "I'm sorry you're feeling this way. Want to talk more about it?",
            "It's okay to feel sad. You're not alone. I'm here for you."
        ])

    elif any(word in user_input for word in anxiety_words):
        return random.choice([
            "Deep breaths can help with anxiety. Want to try a calming exercise?",
            "It’s okay to feel anxious sometimes. Would you like to talk about what’s making you feel this way?"
        ])

    elif any(word in user_input for word in lonely_words):
        return random.choice([
            "You're not alone. I’m here with you. Would you like to share more?",
            "Feeling lonely can be tough. Let’s talk about it together."
        ])

    elif any(word in user_input for word in thanks_words):
        return "You're very welcome. I'm always here to listen. 💙"

    elif "exit" in user_input or "bye" in user_input or "quit" in user_input:
        return "Take care of yourself. You're stronger than you think. Goodbye! 💚"

    else:
        return random.choice([
            "Tell me more about how you're feeling.",
            "I'm listening... feel free to open up.",
            "Would you like to share more details?"
        ])

# Main chatbot loop
def run_chatbot():
    print("🧠 Welcome to the Mental Health Support Chatbot.")
    print("Type 'exit' to leave the chat.\n")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)

        print("Bot:", response)

        if response.startswith("Take care") or user_input.lower() in ["exit", "quit", "bye"]:
            break

# Run chatbot
if __name__ == "__main__":
    run_chatbot()