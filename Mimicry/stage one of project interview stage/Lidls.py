import speech_recognition as sr


class GREET:
    def __init__(self):
        self.Greetings = ["hello", "hi", "how", "are", "today", "going"]

        self.Review = ["trolley", "around", "pull", "bring"]

        self.Evaluate = ["all", "items", "item", "on", "belt",
                         "anything", "in", "trolley"]

        self.Enquire = ["lidl", "plus", "have", "do", "you"]

        self.Thank = ["thank", "you", "shopping", "at", "lidls"]

        self.questions = [
            "Greet the customer",
            "Review the customers trolley placement",
            "Evaluate their trolley, anything left in there",
            "Enquire about Lidl Plus",
            "Thank the customer for shopping at Lidl"
        ]

        self.answer = []


array = GREET()

total_score = 0


def score_Greeting(answer, Greetings):

    score = 0

    words = answer.lower().split()

    for word in words:

        if word in Greetings:
            score += 1

    return score


def score_Review(answer, Review):

    score = 0

    words = answer.lower().split()

    for word in words:

        if word in Review:
            score += 1

    return score


def score_Evaluate(answer, Evaluate):

    score = 0

    words = answer.lower().split()

    for word in words:

        if word in Evaluate:
            score += 1

    return score


def score_Enquire(answer, Enquire):

    score = 0

    words = answer.lower().split()

    for word in words:

        if word in Enquire:
            score += 1

    return score


def score_Thank(answer, Thank):

    score = 0

    words = answer.lower().split()

    for word in words:

        if word in Thank:
            score += 1

    return score


def g():

    global total_score

    recognizer = sr.Recognizer()

    print("\n" + array.questions[0])

    with sr.Microphone() as source:

        print("Speak now...")

        audio = recognizer.listen(source)

    try:

        answer = recognizer.recognize_google(audio)

        print("You said:", answer)

    except:

        answer = ""

        print("Couldn't understand audio")

    score = score_Greeting(answer, array.Greetings)

    total_score += score

    print(f"Answer score: {score}")


def r():

    global total_score

    recognizer = sr.Recognizer()

    print("\n" + array.questions[1])

    with sr.Microphone() as source:

        print("Speak now...")

        audio = recognizer.listen(source)

    try:

        answer = recognizer.recognize_google(audio)

        print("You said:", answer)

    except:

        answer = ""

        print("Couldn't understand audio")

    score = score_Review(answer, array.Review)

    total_score += score

    print(f"Answer score: {score}")


def Ev():

    global total_score

    recognizer = sr.Recognizer()

    print("\n" + array.questions[2])

    with sr.Microphone() as source:

        print("Speak now...")

        audio = recognizer.listen(source)

    try:

        answer = recognizer.recognize_google(audio)

        print("You said:", answer)

    except:

        answer = ""

        print("Couldn't understand audio")

    score = score_Evaluate(answer, array.Evaluate)

    total_score += score

    print(f"Answer score: {score}")


def en():

    global total_score

    recognizer = sr.Recognizer()

    print("\n" + array.questions[3])

    with sr.Microphone() as source:

        print("Speak now...")

        audio = recognizer.listen(source)

    try:

        answer = recognizer.recognize_google(audio)

        print("You said:", answer)

    except:

        answer = ""

        print("Couldn't understand audio")

    score = score_Enquire(answer, array.Enquire)

    total_score += score

    print(f"Answer score: {score}")


def t():

    global total_score

    recognizer = sr.Recognizer()

    print("\n" + array.questions[4])

    with sr.Microphone() as source:

        print("Speak now...")

        audio = recognizer.listen(source)

    try:

        answer = recognizer.recognize_google(audio)

        print("You said:", answer)

    except:

        answer = ""

        print("Couldn't understand audio")

    score = score_Thank(answer, array.Thank)

    total_score += score

    print(f"Answer score: {score}")


def main():

    print("Are you ready?")
    reply = input()

    if reply.lower() == "yes":
        g()
    else:
        print("Okay, skipping")

    print("Are you ready?")
    reply = input()

    if reply.lower() == "yes":
        r()
    else:
        print("Okay, skipping")

    print("Are you ready?")
    reply = input()

    if reply.lower() == "yes":
        Ev()
    else:
        print("Okay, skipping")

    print("Are you ready?")
    reply = input()

    if reply.lower() == "yes":
        en()
    else:
        print("Okay, skipping")

    print("Are you ready?")
    reply = input()

    if reply.lower() == "yes":
        t()
    else:
        print("You're not very good at this")

    print("\nFinal interview score:", total_score)

    if total_score > 5:
        print("Good job, you did really well... I'm proud of you")

    elif total_score > 0:
        print("There were some good points and some bad points")

    else:
        print("That was... might need a little more practice")


main()