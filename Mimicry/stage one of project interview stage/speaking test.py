import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()


def speak():

    engine = pyttsx3.init()

    print("hello")

    engine.say("hello")

    engine.runAndWait()

    engine.stop()
def speak_two():
    engine = pyttsx3.init()
    print("Goodbye")

    engine.say("Goodbye")

    engine.runAndWait()

    engine.stop()

def listen(recognizer):

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


def state_one():

    speak("hello")


def state_two():

    recognizer = sr.Recognizer()

    reply = listen(recognizer)

    print("Reply was:", reply)

    return reply


def main():

    speak()

    reply = state_two()
    speak_two()
main()