from utilities import FileUtilities
from datetime import datetime


def get_frequency(instructions):
    instructions = list(map(int, instructions))

    frequency = 0
    list_of_frequencies = [0]

    instruction_index = 0
    while True:
        frequency_change = instructions[instruction_index]
        frequency += frequency_change

        if frequency in list_of_frequencies:
            print(frequency)
            print("Finish time:", datetime.now())
            break
        else:
            list_of_frequencies.append(frequency)

        instruction_index += 1
        if instruction_index >= len(instructions):
            instruction_index = 0


if __name__ == "__main__":
    input_file_path = "puzzle.in"
    file_content = FileUtilities.get_sanitized_content_from_file(input_file_path)

    print("Start time:", datetime.now())
    get_frequency(file_content)
