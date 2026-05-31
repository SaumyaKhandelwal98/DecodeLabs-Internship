responses = {
    "hello": "Hi there! How can I help you?",
    "hi": "Hello! Nice to meet you.",
    "hey": "Hey! How are you doing?",
    "how are you": "I am doing great. Thanks for asking.",
    "what is your name": "I am DecodeBot, a Rule-Based AI Chatbot.",
    "who created you": "I was created as part of an AI internship project.",
    "what can you do": "I can answer simple predefined questions.",
    "help": "You can ask about my name, creator, AI, Python, or GitHub.",
    "good morning": "Good Morning. Have a productive day.",
    "good afternoon": "Good Afternoon.",
    "good evening": "Good Evening.",
    "good night": "Good Night.",
    "thanks": "You are welcome.",
    "thank you": "Happy to help.",
    "python": "Python is a popular programming language used in AI and software development.",
    "ai": "Artificial Intelligence enables machines to perform tasks that typically require human intelligence.",
    "machine learning": "Machine Learning is a branch of AI that allows systems to learn from data.",
    "github": "GitHub is a platform used for version control and project collaboration.",
    "college": "I am a chatbot, so I do not attend college.",
    "bye": "Goodbye! Have a nice day."
}

print("=" * 50)
print("      DECODEBOT - RULE BASED AI CHATBOT")
print("=" * 50)
print("Type 'bye' to exit the chatbot.")
print()

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "bye":
        print("Bot:", responses["bye"])
        break

    elif user_input in responses:
        print("Bot:", responses[user_input])

    else:
        print("Bot: Sorry, I do not understand that. Type 'help' for available commands.")