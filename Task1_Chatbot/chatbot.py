import datetime

print("AI Chatbot (type 'bye' to exit)")


while True:

    user_input = input("You: ").lower()


    if user_input in ["hello", "hi", "hey"]:
        print("Bot: Hello! Nice to meet you.")

    elif "name" in user_input:
        print("Bot: I am CodSoft AI Chatbot.")

    elif "how are you" in user_input:
        print("Bot: I'm doing great! Hope you're having a good day.")

    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)

    elif "date" in user_input:
        today = datetime.date.today()
        print("Bot: Today's date is", today)

    elif "help" in user_input:
        print("Bot: You can ask me things like:")
        print(" - hello")
        print(" - what is your name")
        print(" - what time is it")
        print(" - what is today's date")


    elif "thank" in user_input:
        print("Bot: You're welcome!")


    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot: Sorry, I don't understand that yet. Try asking something else.")