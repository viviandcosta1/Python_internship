def admission():

    print("Welcome! Let's start the admission inquiry.\n")

    name = input("Chatbot: What is your name? \nYou: ")
    if name == "vvn":
        print("hello vvn welcome to admission inquiry!:")
    else:
        print("your name is not listed:")  

    qualification = input("Chatbot: What is your qualification? \nYou: ")
    if qualification == "puc 2":
        print ("you are eligible for this seat:")
    else:
        print("you are not eligible:")

    year = input("Chatbot: What is your year of passing? \nYou: ") 
    if year >= "2022":
        print("your age is perfect for the admission:")
    else:
        print("your age is not meeting the admission criteria:")

    percentage = input("Chatbot: What is your PUC 2 percentage? \nYou: ")
    if percentage < "90":
        print("your percentage is matching  eligliblity to get the seat:")

    else:
        print("your percentage is  not matching  eligliblity to get the seat") 

    rank = input("Chatbot: What is your CET rank? \nYou: ")
    if rank < "3000":
        print("your admission is conformed!congrats:")  

    else:
        print("sorry your not eligible for govt seat,plese try for managment seat") 

admission()                                     
