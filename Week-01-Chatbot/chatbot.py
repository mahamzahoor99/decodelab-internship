print("maham Welcome to the Rule-Based AI Chatbot!")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I'm fine, thank you!")

    elif user == "what can you do":
        print("Bot: I can answer simple predefined questions.")

    elif user == "your name":
        print("Bot: I am a Rule-Based AI Chatbot.")

    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")