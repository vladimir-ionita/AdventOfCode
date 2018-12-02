from utilities import FileUtilities


def get_difference(word_a, word_b):
    difference = 0
    for c in range(len(word_a)):
        difference += 1 if word_a[c] != word_b[c] else 0
    return difference


def get_similar_words(words):
    for word_index_a in range(len(words)):
        for word_index_b in range(word_index_a + 1, len(words)):
            word_a = words[word_index_a]
            word_b = words[word_index_b]
            if get_difference(word_a, word_b) == 1:
                return word_a, word_b


def get_common_letters(word_a, word_b):
    common = []
    for c in range(len(word_a)):
        if word_a[c] == word_b[c]:
            common.append(word_a[c])
    return ''.join(common)


if __name__ == "__main__":
    input_file_path = "puzzle.in"
    file_content = FileUtilities.get_sanitized_content_from_file(input_file_path)

    word_a, word_b = get_similar_words(file_content)
    print(get_common_letters(word_a, word_b))
