from utilities import FileUtilities
from datetime import datetime
import collections


def get_single_claim(claims):
    picture = collections.defaultdict(int)
    for claim in claims:
        split_raw = claim.split()
        origin_raw = split_raw[2]
        rect_raw = split_raw[3]

        origin_parts = origin_raw[0:-1].split(',')
        origin = (int(origin_parts[0]), int(origin_parts[1]))

        rect_parts = rect_raw.split('x')
        rect = (int(rect_parts[0]), int(rect_parts[1]))

        for i in range(origin[0], origin[0] + rect[0]):
            for j in range(origin[1], origin[1] + rect[1]):
                picture[(i, j)] += 1

    for claim in claims:
        split_parts = claim.split()
        x, y = split_parts[2].split(',')
        x, y = int(x), int(y[:-1])
        w, h = split_parts[3].split('x')
        w, h = int(w), int(h)

        ok = True
        for i in range(w):
            for j in range(h):
                if picture[(i+x, j+y)] > 1:
                    ok = False

        if ok:
            return split_parts[0]


if __name__ == "__main__":
    input_file_path = "puzzle.in"
    file_content = FileUtilities.get_sanitized_content_from_file(input_file_path)

    print("Start time:", datetime.now())
    print(get_single_claim(file_content))
    print("Finish time:", datetime.now())
