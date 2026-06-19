import speech_recognition as sr
import time
import pyttsx3


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


def speak(text):

    engine = pyttsx3.init()

    print(text)

    engine.say(text)

    engine.runAndWait()

    engine.stop()

    time.sleep(0.5)


class QUESTIONING:
    def __init__(self):
        self.Question_one = "Where were you during this time?"
        self.answer_one = []

        self.Question_two = "What were you doing?"
        self.answer_two = []

        self.Question_three = "Who is this person?"
        self.answer_three = []

        self.Question_four = "How do you know ___?"
        self.answer_four = []

        self.Question_five = "Why did you do this?"
        self.answer_five = []

        self.insults = [
            "asshole", "idiot", "moron", "stupid", "dumb",
            "fool", "jerk", "loser", "twit", "nincompoop",
            "imbecile", "cretin", "blockhead", "dunce",
            "nitwit", "simpleton", "clown", "buffoon",
            "dolt", "dimwit", "halfwit", "ignoramus",
            "ninny", "numskull", "pinhead",
            "scatterbrain", "airhead"
        ]


array = QUESTIONING()


def stage_one():

    speak(array.Question_one)
    array.answer_one.append(listen())

    speak(array.Question_two)
    array.answer_two.append(listen())

    speak(array.Question_three)
    array.answer_three.append(listen())

    speak(array.Question_four)
    array.answer_four.append(listen())

    speak(array.Question_five)
    array.answer_five.append(listen())

    speak("Thank you for your time, we'll be in touch.")


def stage_two():

    score = 0

    speak("Please answer the following questions.")

    speak(array.Question_one)
    response_one = listen()

    if any(answer in response_one for answer in array.answer_one):
        score += 1

    speak(array.Question_two)
    response_two = listen()

    if any(answer in response_two for answer in array.answer_two):
        score += 1

    speak(array.Question_three)
    response_three = listen()

    if any(answer in response_three for answer in array.answer_three):
        score += 1

    speak(array.Question_four)
    response_four = listen()

    if any(answer in response_four for answer in array.answer_four):
        score += 1

    speak(array.Question_five)
    response_five = listen()

    if any(answer in response_five for answer in array.answer_five):
        score += 1

    if score > 2:

        speak("Wow, this guy needs to be taken down a peg.")

        insult = listen()

        if any(word in insult for word in array.insults):
            score += 10
        else:
            score -= 10

    return score
def stage_three(total_score):
    if total_score > 15:
        speak("You have been found innocent")
    else:
        speak("You have been found guilty")

def main():
    stage_one()
    total_score = stage_two()
    stage_three(total_score)


if __name__ == "__main__":
    main()