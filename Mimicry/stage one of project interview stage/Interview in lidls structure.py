import time
import pyttsx3
import speech_recognition as sr


def speak(text):

    engine = pyttsx3.init()

    print(text)

    engine.say(text)

    engine.runAndWait()

    engine.stop()

    time.sleep(0.5)


def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        audio = recognizer.listen(
            source,
            timeout=5,
            phrase_time_limit=5
        )

        print("Finished listening")

    try:

        print("Recognizing...")

        text = recognizer.recognize_google(audio)

        print("You said:", text)

        return text.lower()

    except Exception as e:

        print("Error:", e)

        return ""


class Mimicry:
    def __init__(self):

        # question one is hello why don't we start by telling me about yourself.
        self.question_one = [
            "hello", "goodbye", "how", "are",
            "you", "what", "is", "your", "name"
        ]

        # question two why did you apply for this job
        self.question_two = [
            "fit", "motivated", "previous",
            "experience", "gain", "deeper", "insights"
        ]

        # question three what type of skills could you bring to this job
        self.question_three = [
            "motivated",
            "hard", "working", "pace",
            "teamwork", "effective", "communicator"
        ]

        # question four what are your weaknesses
        self.question_four = [
            "perfectionist", "work", "too",
            "hard", "skill"
        ]

        # question five what are your strengths
        self.question_five = [
            "years", "experience",
            "outside", "box"
        ]

        # question six Do you have any questions for us
        self.question_six = [
            "day", "today", "look",
            "like", "work", "environment"
        ]

        self.bad_words = [
            "bad", "hate", "stupid",
            "dumb", "ugly", "umm",
            "uhh", "like", "you",
            "know", "money", "pay"
        ]

        self.questions = [
            "hello why don't we start by telling me about yourself.",
            "why did you apply for this job",
            "what type of skills could you bring to this job",
            "what are your weaknesses",
            "what are your strengths",
            "Do you have any questions for us"
        ]


array = Mimicry()

total_score = 0


def score_question_one(answer, question_one, bad_words):

    score = 0

    words = answer.lower().split()

    for word in words:

        if word in question_one:
            score += 1

        if word in bad_words:
            score -= 1

    return score


def score_question_two(answer, question_two, bad_words):

    score = 0

    words = answer.lower().split()

    for word in words:

        if word in question_two:
            score += 1

        if word in bad_words:
            score -= 1

    return score


def score_question_three(answer, question_three, bad_words):

    score = 0

    words = answer.lower().split()

    for word in words:

        if word in question_three:
            score += 1

        if word in bad_words:
            score -= 1

    return score


def score_question_four(answer, question_four, bad_words):

    score = 0

    words = answer.lower().split()

    for word in words:

        if word in question_four:
            score += 1

        if word in bad_words:
            score -= 1

    return score


def score_question_five(answer, question_five, bad_words):

    score = 0

    words = answer.lower().split()

    for word in words:

        if word in question_five:
            score += 1

        if word in bad_words:
            score -= 1

    return score


def score_question_six(answer, question_six, bad_words):

    score = 0

    words = answer.lower().split()

    for word in words:

        if word in question_six:
            score += 1

        if word in bad_words:
            score -= 1

    return score


def one(question_one, bad_words):

    global total_score

    speak("\n" + array.questions[0])

    answer = listen()

    time.sleep(2)

    score = score_question_one(
        answer,
        question_one,
        bad_words
    )

    total_score += score

    print(f"Question 1 score: {score}")


def two(question_two, bad_words):

    global total_score

    speak("\n" + array.questions[1])

    answer = listen()

    time.sleep(2)

    score = score_question_two(
        answer,
        question_two,
        bad_words
    )

    total_score += score

    print(f"Question 2 score: {score}")


def three(question_three, bad_words):

    global total_score

    speak("\n" + array.questions[2])

    answer = listen()

    time.sleep(2)

    score = score_question_three(
        answer,
        question_three,
        bad_words
    )

    total_score += score

    print(f"Question 3 score: {score}")


def four(question_four, bad_words):

    global total_score

    speak("\n" + array.questions[3])

    answer = listen()

    time.sleep(2)

    score = score_question_four(
        answer,
        question_four,
        bad_words
    )

    total_score += score

    print(f"Question 4 score: {score}")


def five(question_five, bad_words):

    global total_score

    speak("\n" + array.questions[4])

    answer = listen()

    time.sleep(2)

    score = score_question_five(
        answer,
        question_five,
        bad_words
    )

    total_score += score

    print(f"Question 5 score: {score}")


def six(question_six, bad_words):

    global total_score

    speak("\n" + array.questions[5])

    answer = listen()

    time.sleep(2)

    score = score_question_six(
        answer,
        question_six,
        bad_words
    )

    total_score += score

    print(f"Question 6 score: {score}")


def main():

    one(array.question_one, array.bad_words)

    two(array.question_two, array.bad_words)

    three(array.question_three, array.bad_words)

    four(array.question_four, array.bad_words)

    five(array.question_five, array.bad_words)

    six(array.question_six, array.bad_words)

    print(f"Final score: {total_score}")

    speak(f"Your final score was {total_score}")


main()