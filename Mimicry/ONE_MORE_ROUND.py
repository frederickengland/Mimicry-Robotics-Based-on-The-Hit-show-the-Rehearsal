import speech_recognition as sr
import time
import pyttsx3
import serial
# Okay I'm going to use this as a scene and how to script things out.

# Arduino connection
arduino = serial.Serial(
    port='COM9',
    baudrate=115200,
    timeout=.1
)


def speak(text):
    engine = pyttsx3.init()
    print(text)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    time.sleep(0.5)


def light_one():
    arduino.write(b'1')
    time.sleep(0.05)
    return arduino.readline()


def light_one_off():
    arduino.write(b'0')
    time.sleep(0.05)
    return arduino.readline()


def light_two():
    arduino.write(b'2')      # Fixed: c'1' -> b'2'
    time.sleep(0.05)
    return arduino.readline()


def light_two_off():
    arduino.write(b'3')
    time.sleep(0.05)
    return arduino.readline()


class ONE_MORE_ROUND:
    def __init__(self):
        self.part_one = light_one()
        self.part_two = (
            "I've got trademark products all over my body because I was drunk one night. "
            "Don't live like me."
        )
        self.part_three = light_one_off()
        self.part_four = light_two()
        self.part_five = (
            "You know, I mean, uh, kids don't want to do anything. "
            "You know, in my experience, Paula? Kids are always like "
            "\"I don't wanna do that!\" "
            "I consider my job to kinda twist them in the direction of doing stuff. "
            "I mean that's what coaching's all about. That's why I love it. "
            "Every day I go out there and I twist the kids into doing something "
            "they don't wanna do!"
        )
        self.part_six = light_two_off()


array = ONE_MORE_ROUND()


def main():
    light_one()
    speak(array.part_two)
    light_one_off()
    light_two()
    speak(array.part_five)
    light_two_off()

if __name__ == "__main__":
    main()