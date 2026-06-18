print("Chatbot Started")

while True:
    user = input("You: ")

    if user == "hi":
        print("Bot: Hello")

    elif user == "how are you":
        print("Bot: I am fine")

    elif user == "bye":
        print("Bot: Goodbye")
        break

    else:
        print("Bot: I don't know")
