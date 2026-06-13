import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()


class Mimicry:
    def __init__(self):

        self.good_words = []
        self.bad_words = []

        self.questions = [
            "Tell me about yourself.",
            "What's one of your weaknesses?",
            "What's one of your strengths?",
            "What's your greatest achievement?",
            "Where do you see yourself in 5 years?"
        ]


array = Mimicry()


def speak(text):

    print(text)

    engine.say(text)

    engine.runAndWait()


def load_words(filename):

    words = []

    try:
        with open(filename, "r") as file:

            for word in file.read().split():
                words.append(word.lower())

    except FileNotFoundError:
        print(f"Could not open {filename}")

    return words


def score_answer(answer, good_words, bad_words):

    score = 0

    words = answer.lower().split()

    for word in words:

        if word in good_words:
            score += 1

        if word in bad_words:
            score -= 1

    return score


def listen(recognizer):

    with sr.Microphone() as source:

        recognizer.adjust_for_ambient_noise(source, duration=1)

        audio = recognizer.listen(source)

    try:

        text = recognizer.recognize_google(audio)

        print("You said:", text)

        return text.lower()

    except:

        print("Could not understand audio")

        return ""


def main():

    array.good_words = load_words("good_words.txt")
    array.bad_words = load_words("bad_words.txt")

    recognizer = sr.Recognizer()

    total_score = 0

    for question in array.questions:

        speak("Are you ready? Say yes to continue.")
        speak("speak now")
        reply = listen(recognizer)

        if "yes" not in reply:
            speak("Okay, skipping")
            continue

        speak(question)

        speak("Speak now.")

        answer = listen(recognizer)

        score = score_answer(
            answer,
            array.good_words,
            array.bad_words
        )

        total_score += score

        speak(f"Answer score: {score}")

    speak(f"Final interview score: {total_score}")

    if total_score > 5:
        speak("Good job, you did really well. I'm proud of you")

    elif total_score > 0:
        speak("There were some good points and some bad points")

    else:
        speak("That was. You might need a little more practice")


main()