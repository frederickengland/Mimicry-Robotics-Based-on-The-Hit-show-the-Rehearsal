import pyttsx3
import speech_recognition as sr


def speak(text):

    engine = pyttsx3.init()

    print(text)

    engine.say(text)

    engine.runAndWait()

    engine.stop()


def main():

    speak("hello")

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        audio = recognizer.listen(
            source,
            timeout=5,
            phrase_time_limit=5
        )

    print("Finished listening")

    speak("goodbye")


main()