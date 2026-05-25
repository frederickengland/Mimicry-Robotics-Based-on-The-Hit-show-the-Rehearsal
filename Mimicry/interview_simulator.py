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


def main():

    array.good_words = load_words("good_words.txt")
    array.bad_words = load_words("bad_words.txt")

    total_score = 0

    for question in array.questions:

        print("\n" + question)

        answer = input("> ")

        score = score_answer(
            answer,
            array.good_words,
            array.bad_words
        )

        total_score += score

        print(f"Answer score: {score}")

    print("\nFinal interview score:", total_score)

    if total_score > 5:
        print("Good job, you did really well... I'm proud of you")

    elif total_score > 0:
        print("There were some good points and some bad points")

    else:
        print("That was... might need a little more practice")


main()