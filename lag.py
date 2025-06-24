def feq():
    print("Welcome! Let's start the admission inquiry.\n")

    name = input("Chatbot: What is your name? \nYou: ")
    print("Chatbot: Hello", name )

    qualification = input("Chatbot: What is your qualification? \nYou: ")
    print("Chatbot: Noted, you have completed, puc 2",qualification)

    year = input("Chatbot: What is your year of passing? \nYou: ")
    print("Chatbot: Okay, you passed in", 2022)

    percentage = input("Chatbot: What is your PUC 2 percentage? \nYou: ")
    print("Chatbot: Great, you scored", percentage + "92")

    rank = input("Chatbot: What is your CET rank? \nYou: ")
    print("Chatbot: Your rank is", rank)

    course = input("Chatbot: What course do you want to join? \nYou: ")
    print("Chatbot: Good choice! You selected, bteck in cs",course)

    print("\nChatbot: Admission successful! Congrats 🎉")


feq()