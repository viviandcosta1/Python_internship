from nltk.chat.util import Chat, reflections

# Define some simple patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created with NLTK.", "You can call me NLTK Bot."]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I am just a bot, but I'm good!"]
    ],
    [
        r"sorry (.*)",
        ["It's okay.", "No problem!", "Don't worry about it."]
    ],
    [
        r"(.*) help (.*)",
        ["I can help you. Just ask me anything!", "Sure, I'm here to help."]
    ],
    [
        r"quit|bye|exit",
        ["Bye! Have a nice day.", "Goodbye!", "See you later!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand.", "Can you say that again?", "Let's talk about something else."]
    ]
]

# Create a chatbot instance
def chatbot():
    print("Hi! I'm your chatbot. Type 'quit' or 'bye' to exit.\n")
    chat = Chat(pairs, reflections)
    chat.converse()

# Run the chatbot
if __name__ == "__main__":
    chatbot()