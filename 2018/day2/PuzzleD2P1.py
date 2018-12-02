from utilities import FileUtilities


def get_canonic_form(word):
    import collections

    dictionary = collections.defaultdict(int)
    for character in word:
        dictionary[character] += 1
    return dictionary


def does_word_contain_double_and_triple_letter(word):
    canonic_form = get_canonic_form(word)

    double_letters = False
    triple_letters = False
    for key, value in canonic_form.items():
        if value == 2:
            double_letters = True
        if value == 3:
            triple_letters = True

    return double_letters, triple_letters


def get_checksum(words):
    double_letters_words = 0
    triple_letters_words = 0

    for word in words:
        word_dt_results = does_word_contain_double_and_triple_letter(word)
        double_letters_words += 1 if word_dt_results[0] else 0
        triple_letters_words += 1 if word_dt_results[1] else 0
    return double_letters_words * triple_letters_words


if __name__ == "__main__":
    input_file_path = "puzzle.in"
    file_content = FileUtilities.get_sanitized_content_from_file(input_file_path)

    print(get_checksum(file_content))
