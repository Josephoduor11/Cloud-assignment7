message = input(">")

words = message.split()

emojis = {
    ":)": "☺️",
    ":(": "☹️",
    ":|": "😐"
}


def emoji_converter(words):
    Results = " "

    for x in range(len(words)):
        if words[x].isalpha():
            Results += words[x] + " "

        if words[x] == ":)":
            Results += emojis.get(":)") + " "
        elif words[x] == ":(":
            Results += emojis.get(":(") + " "
        elif words[x] == ":|":
            Results += emojis.get(":|") + " "

    print(Results)


emoji_converter(words)
