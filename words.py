def print_upper_words(words):
    """Print each word on sep line, uppercased.
    """

    for word in words:
        print(word.upper())


def print_words_e(words):
    """Print each word on sep line, uppercased, if starts with E or e.
    """

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


def print_upper_words3(words, letters):
    """Print each word on sep line, uppercased, if starts with one of given
    """

    for word in words:
        for letter in letters:
            if word.startswith(letter):
                print(word.upper())
                break
