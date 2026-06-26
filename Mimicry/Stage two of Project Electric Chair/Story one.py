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
        # More inventive and story driven questions / questions too generic
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


array = QUESTIONING()


class TRIAL:
    def __init__(self):
        self.question_one = "Where were you during this time?"
        self.answer_one = array.answer_one

        self.question_two = "What were you doing?"
        self.answer_two = array.answer_two

        self.question_three = "Who is this person?"
        self.answer_three = array.answer_three

        self.question_four = "How do you know ___?"
        self.answer_four = array.answer_four

        self.question_five = "Why did you do this?"
        self.answer_five = array.answer_five

        self.insults = [
            "asshole", "idiot", "moron", "stupid", "dumb",
            "fool", "jerk", "loser", "twit", "nincompoop",
            "imbecile", "cretin", "blockhead", "dunce",
            "nitwit", "simpleton", "clown", "buffoon",
            "dolt", "dimwit", "halfwit", "ignoramus",
            "ninny", "numskull", "pinhead",
            "scatterbrain", "airhead"
        ]


trial_array = TRIAL()


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
    array.answer_one = listen()

    speak(array.question_two)
    array.answer_two = listen()

    speak(array.question_three)
    array.answer_three = listen()

    speak(array.question_four)
    array.answer_four = listen()

    speak(array.question_five)
    array.answer_five = listen()


def scene_two():

    score = 0

    speak(array.question_one)
    response_one = listen()

    if array.answer_one in response_one:
        score += 1
    else:
        score -= 1

    speak(array.question_two)
    response_two = listen()

    if array.answer_two in response_two:
        score += 1
    else:
        score -= 1

    speak(array.question_three)
    response_three = listen()

    if array.answer_three in response_three:
        score += 1
    else:
        score -= 1

    speak(array.question_four)
    response_four = listen()

    if array.answer_four in response_four:
        score += 1
    else:
        score -= 1

    speak(array.question_five)
    response_five = listen()

    if array.answer_five in response_five:
        score += 1
    else:
        score -= 1

    if score > 3:

        speak("Why don't you just insult me")

        insult = listen()

        if insult in trial_array.insults:
            score += 5
        else:
            score -= 5

    print("Score:", score)

    return score


def stage_three(total_score):

    if total_score > 15:
        speak("You have been found innocent")
    else:
        speak("You have been found guilty")


def main():

    print("Are you ready?")
    answer = input()

    if answer.lower() == "y":

        scene_one()

        total_score = scene_two()

        stage_three(total_score)

    else:

        stage_three(0)


main()