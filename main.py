from nltk.chat.util import Chat, reflections

expressions = [
    [
        r"my name is (.*)",
        ["Hello %1! How are you today ?", ]
    ],
    [
        r"(.*) Turing test",
        ["Can you?", ]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there", ]
    ],
    [
        r"what is your name ?",
        ["I am a bot created by Dimitar Madjarov. you can call me crazy!", ]
    ],
    [
        r"how are you ?",
        ["I'm doing good \nHow about You ?", ]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind", ]
    ],
    [
        r"I'm fine",
        ["Great to hear that! How can I help you?", ]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that", "How can I help you?:)", ]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program my friend... \nAre you seriously asking me this?", ]
    ],
    [
        r"(.*) old are you?",
        ["I'm a computer program friend... \nAre you seriously asking me this?", ]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse :)", ]
    ],
    [
        r"(.*) created ?",
        ["Dimitar created me using Python's NLTK library - top secret ;)", ]
    ],
    [
        r"(.*) (location|city) ?",
        ['Sofia City', ]
    ],
    [
        r"how is the weather in (.*)?",
        ["Weather in %1 is awesome like always", "Too hot here in %1", "Too cold here in %1",
         "Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days, aren't they.", ]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2", "It's raining too much here in %2"]
    ],
    [
        r"how(.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ", ]
    ],
    [
        r"(.*) (sport|game) ?",
        ["I'm a very big fan of Football", ]
    ],
    [
        r"(.*) color ?",
        ["I like blue, and you?", ]
    ],
    [
        r"who(.*) player?",
        ["Messy", "Ronaldo", "Rooney"]
    ],
    [
        r"who(.*) (movie star|actor)?",
        ["Brad Pitt"]
    ],
    [
        r"I like (.*)",
        ["That's great, I love %1 too."]
    ],
    [
        r"I love (.*)",
        ["That's great, me too!"]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon :) ", "It was nice talking to you. See you soon :)"]
    ],
    [
        r"bye",
        ["Bye, take care. See you soon :) ", "It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ["I didn't understand that."]
    ],
]


def chat():
    print("Hi! I am a chatbot created by Dimitar Madjarov for your service.")
    chatting = Chat(expressions, reflections)
    chatting.converse()


if __name__ == "__main__":
    chat()
