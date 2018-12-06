from utilities import FileUtilities
import collections

input_file_path = "puzzle.in"
S = FileUtilities.get_sanitized_content_from_file(input_file_path)


def get_distance(a, b):
    return abs(b[0]-a[0]) + abs(b[1] - a[1])


def get_closest(point, list):
    results = []
    for p in list:
        results.append(get_distance(p, point))

    min_d = min(results)
    indices = [i for i, x in enumerate(results) if x == min_d]
    if len(indices) > 1:
        return -1
    else:
        return indices[0]


def get_vertical_distance(c1, c2):
    return abs(c2[0] - c1[0])


def get_horizontal_distance(c1, c2):
    return abs(c2[1] - c1[1])


coordinates = []
for i in S:
    x, y = i.split(',')
    x, y = int(x), int(y)
    coordinates.append((x, y))


finite = []
for c in coordinates:
    q1 = []
    q2 = []
    q3 = []
    q4 = []
    for c1 in coordinates:
        if c1[0] < c[0] and c1[1] < c[1]:
            q1.append(c1)
        elif c1[0] < c[0] and c1[1] > c[1]:
            q2.append(c1)
        elif c1[0] > c[0] and c1[1] > c[1]:
            q3.append(c1)
        elif c1[0] > c[0] and c1[1] < c[1]:
            q4.append(c1)

    if not q1 or not q2 or not q3 or not q4:
        continue

    for c1 in q1:
        if get_horizontal_distance(c, c1) < get_vertical_distance(c, c1):
            continue
    for c1 in q2:
        if get_horizontal_distance(c, c1) < get_vertical_distance(c, c1):
            continue

    for c1 in q2:
        if get_vertical_distance(c, c1) < get_horizontal_distance(c, c1):
            continue
    for c1 in q3:
        if get_vertical_distance(c, c1) < get_horizontal_distance(c, c1):
            continue

    for c1 in q3:
        if get_horizontal_distance(c, c1) < get_vertical_distance(c, c1):
            continue
    for c1 in q4:
        if get_horizontal_distance(c, c1) < get_vertical_distance(c, c1):
            continue

    for c1 in q4:
        if get_vertical_distance(c, c1) < get_horizontal_distance(c, c1):
            continue
    for c1 in q1:
        if get_vertical_distance(c, c1) < get_horizontal_distance(c, c1):
            continue

    finite.append(c)


rows, _ = max(coordinates, key=lambda x: x[0])
_, cols = max(coordinates, key=lambda x: x[1])
rows += 1
cols += 1

grid = [[-2 for _ in range(cols)] for _ in range(rows)]

M = collections.defaultdict(int)
for i in range(rows):
    for j in range(cols):
        closest_point = get_closest((i, j),  coordinates)
        grid[i][j] = closest_point
        M[closest_point] += 1


M1 = {}
for c in finite:
    M1[coordinates.index(c)] = M[coordinates.index(c)]

print(max(M1.items(), key=lambda x: x[1]))
