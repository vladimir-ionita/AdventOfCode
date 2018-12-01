from utilities import FileUtilities


def get_frequency(instructions):
    instructions = list(map(int, instructions))
    return sum(instructions)


if __name__ == "__main__":
    input_file_path = "puzzle.in"
    file_content = FileUtilities.get_sanitized_content_from_file(input_file_path)

    print(get_frequency(file_content))
