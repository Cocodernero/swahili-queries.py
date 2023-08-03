# a dictionary that stores questions and answers
# have a variable that tracks the score of the player
# loop through the dictionary using the key values pairs
# display each question to the user and allow them to answer
# tell them if they are right or wrong
# show the final results when the quiz is over

quiz = {
    "swali1": {
        "swali": "haraka haraka haina?",
        "jibu": "baraka"
    },

    "swali2": {
        "swali": "Ruto ndye?",
        "jibu": "Mkuu"
    },

    "swali3": {
        "swali": "Baba alisema aje?",
        "jibu": "Rao"
    },

    "swali4": {
        "swali": "Uganda iko?",
        "jibu": "Kusini"
    },

    "swali5": {
        "swali": "Magharibi ni side gani?",
        "jibu": "East"
    },

    "swali6": {
        "swali": "mamode wawache?",
        "jibu": "Utiaji"
    },

    "swali7": {
        "swali": "guza?",
        "jibu": "imwage"
    }
}

score = 0

for key,value in quiz.items():
    print(value["swali"])
    answer = input("jibu? ")

    if answer.lower() == value["jibu"].lower():
        print("nare")
        score = score + 1
        print("umepata point: " + str(score))
        print("")
        print("")

    else:
        print("buda hizi ndyo gani!")
        print("jibu ndyo hii : " + value["jibu"])
        print("umepata point: " + str(score))
        print("")
        print("")

print("umepata " + str(score) + " kwa maswali 7")
print("umepata percentage ya " + str(int(score/7 * 100)) + "%")