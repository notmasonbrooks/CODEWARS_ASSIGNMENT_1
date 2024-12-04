# Even or Odd


def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Convert a Number to a String


def number_to_string(num):
    str_num = str(num)
    return str_num


# Vowel Count


def get_count(sentence):
    vowels = ["a", "e", "i", "o", "u"]
    vowel_count = 0
    for char in sentence:
        if char in vowels:
            vowel_count += 1
    return vowel_count
