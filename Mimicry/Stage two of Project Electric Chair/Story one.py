import speech_recognition as sr
import time
import pyttsx3
import serial

# Arduino connection
arduino = serial.Serial(
    port='COM9',
    baudrate=115200,
    timeout=.1
)


class QUESTIONING:
    def __init__(self):
        #More inventive and story driven questions / questions too generic
        self.question_one = "Where were you during this time?"
        self.answer_one = ""

        self.question_two = "What were you doing?"
        self.answer_two = ""

        self.question_three = "Who is this person?"
        self.answer_three = ""

        self.question_four = "How do you know ___?"
        self.answer_four = ""

        self.question_five = "Why did you do this?"
        self.answer_five = ""

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


def light_on():
    arduino.write(b'1')
    time.sleep(0.05)
    return arduino.readline()


def light_off():
    arduino.write(b'0')
    time.sleep(0.05)
    return arduino.readline()


def music_start():
    arduino.write(b'2')
    time.sleep(0.05)
    return arduino.readline()


def music_off():
    arduino.write(b'3')
    time.sleep(0.05)
    return arduino.readline()


def scene_one():  # key gameplay loop
    speak(array.question_one)
    response = listen()

    if response == array.answer_one:
        light_on()
        music_start()

    else:
        music_off()
        light_off()


    return


scene_one()