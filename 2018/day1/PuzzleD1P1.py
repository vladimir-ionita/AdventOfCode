from utilities import FileUtilities


def get_frequency(instructions):
    frequency = 0
    while len(instructions) > 0:
        frequency_change = int(instructions.pop(0))
        frequency += frequency_change
    return frequency


if __name__ == "__main__":
    input_file_path = "puzzle.in"
    file_content = FileUtilities.get_sanitized_content_from_file(input_file_path)

    print(get_frequency(file_content))
