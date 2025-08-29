def get_reply(message):
    message = message.lower()
    if message == "hello" or message == "hi":
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message == "bye" or message == "goodbye":
        return "Goodbye!"
    else:
        return "I didn't understand that. Please try again!"

def chatbot():
    print("Welcome to the chatbot! Type 'bye' to exit.")
    while True:
        message = input("You: ")
        if message.lower() == "bye":
            print("Chatbot: Goodbye!")
            break