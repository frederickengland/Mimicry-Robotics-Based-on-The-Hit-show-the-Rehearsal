import speech_recognition as sr
import time
import pyttsx3


class WHATEVER_IT_TAKES:
    def __init__(self):
        # More inventive and story driven questions
        self.question_one = "You just gonna lie there"
        self.answer_one = (
            "no", "can't", "stuck", "help", "please",
            "i can't move", "i can't breathe", "i can't see",
             "i can't feel",
             "i can't speak", "i can't do anything"
        )

        self.question_two = "Just tell me when and I'll stop, I'll ring the bell. That's it"
        self.answer_two = (
            "stop", "please stop",
            "i can't take it anymore",
            "i can't do this",
            "i can't handle this",
            "i can't bear this",
            "i can't endure this",
            "i can't survive this"
        )

        self.question_three = "So you're giving up, huh?"
        self.answer_three = (
            "yes",
            "i guess",
            "i don't know",
            "i just can't anymore",
            "i'm tired",
            "i'm done"
        )


array = WHATEVER_IT_TAKES()


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


def one_more_round():

    score = 0

    speak("Please answer the following questions.")

    speak(array.question_one)
    response_one = listen()

    if any(answer in response_one for answer in array.answer_one):
        score -= 1
    else:
        score += 1

    speak(array.question_two)
    response_two = listen()

    if any(answer in response_two for answer in array.answer_two):
        score -= 1
    else:
        score += 1

    speak(array.question_three)
    response_three = listen()

    if any(answer in response_three for answer in array.answer_three):
        score += 1
    else:
        score -= 1

    return score


def no_more_round():

    total_score = one_more_round()

    if total_score > 1:
        speak("One more round.")
        speak("Whatever it takes.")
        speak("Give me one more round.")

        final_chance = listen()

        if any(answer in final_chance for answer in
               (array.answer_one + array.answer_two + array.answer_three)):
            speak("Then stay down. You've given up.")
        else:
            speak("You got back up. Now show them you've got gas in the tank.")

    else:
        speak("If you can get up, get up and show them how hard you've worked.")
        speak("Show them you can get knocked down and get back up.")


def main():

    no_more_round()


if __name__ == "__main__":
    main()