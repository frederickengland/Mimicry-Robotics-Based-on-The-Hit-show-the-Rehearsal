# Importing Libraries
import serial
import time
import pyttsx3
import speech_recognition as sr

# Arduino connection
arduino = serial.Serial(
    port='COM9',
    baudrate=115200,
    timeout=.1
)


def write_read(x):

    arduino.write(bytes(x, 'utf-8'))

    time.sleep(0.05)

    data = arduino.readline()

    return data


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

        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        audio = recognizer.listen(
            source,
            timeout=5,
            phrase_time_limit=5
        )

    try:

        text = recognizer.recognize_google(audio)

        print("You said:", text)

        return text.lower()

    except Exception as e:

        print("Error:", e)

        return ""


def main():

    speak("hello")

    reply = listen()

    print("Reply was:", reply)

    if reply == "hello":

        print("light on")

        value = write_read("1")

        print(value)

    else:

        print("light off")

        value = write_read("0")

        print(value)

    print("Waiting before speaking again...")

    time.sleep(2)

    speak("goodbye")

    print("Test complete")


main()