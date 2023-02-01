import json
from random import randint


numbers = [
    ["ゼロ", "ゼロ"],
    ["一", "いち"],
    ["二", "に"],
    ["三", "さん"],
    ["四", "よん"],
    ["五", "ご"],
    ["六", "ろく"],
    ["七", "なな"],
    ["八", "はち"],
    ["九", "きゅう"],
    ["十", "じゅう"],
    ["百", "ひゃく"]
]


def conv_num(kana_sys, n):
    num_digits = [int(x) for x in str(n)]
    jp_num = ""
    if n <= 10:
        return numbers[n][kana_sys]
    elif n < 100:
        if kana_sys:
            if num_digits[0] > 1:
                jp_num += numbers[num_digits[0]][1]
            jp_num += numbers[10][1]
            if num_digits[1] > 0:
                jp_num += numbers[num_digits[1]][1]
        else:
            if num_digits[0] > 1:
                jp_num += numbers[num_digits[0]][0]
            jp_num += numbers[10][0]
            if num_digits[1] > 0:
                jp_num += numbers[num_digits[1]][0]
    else:
        if kana_sys:
            if num_digits[0] > 1:
                jp_num += numbers[num_digits[0]][1]
            jp_num += numbers[11][1]
            if num_digits[1] > 1:
                jp_num += numbers[num_digits[1]][1]
                jp_num += numbers[10][1]
            if num_digits[2] > 0:
                jp_num += numbers[num_digits[2]][1]
        else:
            if num_digits[0] > 1:
                jp_num += numbers[num_digits[0]][0]
            jp_num += numbers[11][0]
            if num_digits[1] > 1:
                jp_num += numbers[num_digits[1]][0]
                jp_num += numbers[10][0]
            if num_digits[2] > 0:
                jp_num += numbers[num_digits[2]][0]
    return jp_num


def ask_num(kana_sys, max_number):
    numbers_asked = []
    while True:
        if len(numbers_asked) == max_number:
            print("Good job! All numbers are finished :)")
            break

        # generate random number between 0 and user maximum input
        n = randint(0, max_number)
        # loop until novel number is picked
        while n in numbers_asked:
            n = randint(0, max_number)
        result_num = conv_num(kana_sys, n)
        print("Which number is the following character?")
        print(result_num)
        correct_guess = False
        # loop until user enters correct number or types 'help'
        while not correct_guess:
            usr_number = input()
            if usr_number == "help":
                print("The correct answer is:")
                print(n)
                correct_guess = True
            elif int(usr_number) == n:
                print("Correct! Nice done!")
                correct_guess = True
                numbers_asked.append(n)
            else:
                print("Unfornately wrong, try again :)")
                print(result_num)


def pract_num():
    print("What is the highest number you want to practice between 1 and 999?")
    corr_input = False
    while not corr_input:
        input_num = input()

        if not input_num.isnumeric():
            print("Please enter numbers only")
        elif int(input_num) < 1:
            print("Please enter a number bigger than 0")
        elif int(input_num) > 999:
            print("Please enter a number less than 1000")
        else:
            print("Do you want to practice kanji or kana?")
            while not corr_input:
                input_str = input()
                if input_str == "kanji":
                    corr_input = True
                    ask_num(0, int(input_num))
                elif input_str == "kana":
                    corr_input = True
                    ask_num(1, int(input_num))
                else:
                    print("Please type only 'kanji' or 'kana'")


def pract_meaning():
    with open("data/kanjisv2.json", "r") as jsonFile:
        kanji_list = json.load(jsonFile)

    words_asked = []
    max_number = len(kanji_list)

    while True:
        if len(words_asked) == max_number:
            print("Good job! All words are finished :)")
            break

        # generate random number and pick a kanji
        n = randint(0, max_number - 1)
        kanji = kanji_list[n]
        # loop until novel kanji is chosen
        while kanji["kanji"] in words_asked:
            n = randint(0, max_number - 1)
            kanji = kanji_list[n]

        kanji = kanji["examples"].split("\n")
        # sometimes multiple examples, pick one randomly
        m = randint(0, len(kanji) - 1)
        # split kanji example into kanji, hiragana and english meaning
        kanji = kanji[m].split(",")
        kanji_jp = kanji[0] + " " + kanji[1]
        kanji_en = kanji[2]
        correct_answers = kanji_en.lower().split("/")

        print("What does the following kanji example mean?")
        print(kanji_jp)
        input_str = input()
        next_kanji = False
        # loop until user enters correct meaning or types 'help'
        while not next_kanji:
            if input_str in correct_answers:
                print("Correct! Well done!")
                next_kanji = True
            elif input_str == "help":
                print("The correct answer(s):")
                print(kanji_en)
                next_kanji = True
            else:
                print("Not quite right, try again :)")
                print(kanji_jp)
                input_str = input()
        # add to asked kanji list
        words_asked.append(kanji["kanji"])

def pract_reading():
    with open("data/kanjisv2.json", "r") as jsonFile:
        kanji_list = json.load(jsonFile)

    words_asked = []
    max_number = len(kanji_list)

    while True:
        if len(words_asked) == max_number:
            print("Good job! All words are finished :)")
            break

        # generate random number and pick a kanji
        n = randint(0, max_number - 1)
        kanji = kanji_list[n]
        # loop until novel kanji is chosen
        while kanji["kanji"] in words_asked:
            n = randint(0, max_number - 1)
            kanji = kanji_list[n]

        words_asked.append(kanji["kanji"])
        kanji = kanji["examples"].split("\n")
        # sometimes multiple examples, pick one randomly
        m = randint(0, len(kanji) - 1)
        # split kanji example into kanji, hiragana and english meaning
        kanji = kanji[m].split(",")
        kanji_raw = kanji[0] + " - " + kanji[2]
        kanji_reading = kanji[1]

        print("What do you read the following kanji example?")
        print(kanji_raw)
        input_str = input()
        next_kanji = False
        # loop until user enters correct reading or types 'help'
        while not next_kanji:
            if input_str == kanji_reading:
                print("Correct! Well done!")
                next_kanji = True
            elif input_str == "help":
                print("The correct answer(s):")
                print(kanji_reading)
                next_kanji = True
            else:
                print("Not quite right, try again :)")
                print(kanji_raw)
                input_str = input()


def pract_words():
    print("Do you want to practice the meaning or the reading?")
    corr_input = False
    while not corr_input:
        input_str = input()
        if input_str == "meaning":
            corr_input = True
            pract_meaning()
        elif input_str == "reading":
            corr_input = True
            pract_reading()
        else:
            print("Please type only 'meaning' or 'reading'")


def usr_input():
    print("Do you want to practice numbers or words?")
    corr_input = False
    while not corr_input:
        input_str = input()
        # use match case with python 3.10
        if input_str == "numbers":
            corr_input = True
            pract_num()
        elif input_str == "words":
            corr_input = True
            pract_words()
        else:
            print("Please type only 'numbers' or 'words'")


if __name__ == "__main__":
    try:
        usr_input()
    except KeyboardInterrupt:
        print("Have a nice day :)")
        pass
