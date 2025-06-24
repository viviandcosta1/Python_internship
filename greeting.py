def greet():
    print("Welcome! Let's start the conversation.\n")

    name = input("chatbot:what is your name ?\nYou:")
    if name == "vivian":
        print("hello vivian:")
    else:
        print("plese enter a valid name:") 

    mood = input("Chatbot: How are you feeling today? \nYou: ")
    if mood == "very good":
        print("nice to here it :")

    else:
        print("plese enter your right mood:")

    time_of_day = input("Chatbot: What time of the day is it? (morning/afternoon/evening) \nYou: ")
    if  time_of_day == "morning":
        print("thank you for letting me know:")

    else:
        print("invalid time_of_day:")

    health = input("Chatbot:how is your health? \nYou: ")

    if health == "alright":
        print("your strong:")

    else:
        print("take care of yourself:")    


greet()               