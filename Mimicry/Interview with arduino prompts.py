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

        self.goodwords = [
            "hello", "goodbye", "how", "are",
            "you", "what", "is", "your", "name"
        ]

        self.badwords = [
            "bad", "hate", "stupid",
            "dumb", "ugly"
        ]

        self.questions = [
            "how are you",
            "what is your name"
        ]


array = Mimicry()


def load_words(filename):

    words = []

    try:

        with open(filename, "r") as file:

            for word in file.read().split():

                words.append(word.lower())

    except FileNotFoundError:

        print(f"File not found: {filename}")

    return words


def score_answer(answer, good_words, bad_words):

    score = 0

    if not answer:

        return score

    words = answer.lower().split()

    for word in words:

        if word in good_words:

            score += 1

        if word in bad_words:

            score -= 1

    return score


def main():

    total_score = 0

    # Uncomment these later if you want to load from files
    # array.goodwords = load_words("good_words.txt")
    # array.badwords = load_words("bad_words.txt")

    for question in array.questions:

        speak(question)

        answer = listen()

        time.sleep(2)

        score = score_answer(
            answer,
            array.goodwords,
            array.badwords
        )

        total_score += score

        print(f"Score for answer: {score}")

        speak(f"Your score was {score}")
        if score <= 0:
            print("Lights brighter")
        else:
            print("Light more relaxed")
    print(f"Final score: {total_score}")

    speak(f"Your final score was {total_score}")


main()