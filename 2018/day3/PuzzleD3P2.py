from utilities import FileUtilities


def is_claim_overlapped(claim, final_array):
    for i in range(claim[0][0], claim[0][0] + claim[1][0]):
        for j in range(claim[0][1], claim[0][1] + claim[1][1]):
            if final_array[i][j] > 1:
                return True
    return False


def get_result(claims):
    final_array_rect = (0, 0)

    sanitized_claims = []
    for claim in claims:
        result_raw = claim.split()
        claim_origin = result_raw[2]
        claim_rect = result_raw[3]

        origin_raw = claim_origin[0:-1].split(",")
        origin = (int(origin_raw[0]), int(origin_raw[1]))

        rect_raw = claim_rect.split("x")
        rect = (int(rect_raw[0]), int(rect_raw[1]))

        sanitized_claims.append((origin, rect))

        if origin[0] + rect[0] > final_array_rect[0]:
            final_array_rect = (origin[0] + rect[0], final_array_rect[1])
        if origin[1] + rect[1] > final_array_rect[1]:
            final_array_rect = (final_array_rect[0], origin[1] + rect[1])

    final_array = [[0 for x in range(final_array_rect[0] + 1)] for y in range(final_array_rect[1] + 1)]
    for claim in sanitized_claims:
        for i in range(claim[0][0], claim[0][0] + claim[1][0]):
            for j in range(claim[0][1], claim[0][1] + claim[1][1]):
                final_array[i][j] += 1

    area = 0
    for i in range(0, final_array_rect[0]):
        for j in range(0, final_array_rect[1]):
            area += 1 if final_array[i][j] >= 2 else 0

    for claim in sanitized_claims:
        if not is_claim_overlapped(claim, final_array):
            print(sanitized_claims.index(claim) + 1)


if __name__ == "__main__":
    input_file_path = "puzzle.in"
    file_content = FileUtilities.get_sanitized_content_from_file(input_file_path)

    get_result(file_content)
