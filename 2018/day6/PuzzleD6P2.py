from utilities import FileUtilities


def get_distance(a, b):
    return abs(b[0]-a[0]) + abs(b[1] - a[1])


input_file_path = "puzzle.in"
S = FileUtilities.get_sanitized_content_from_file(input_file_path)

coordinates = []
for i in S:
    x, y = i.split(',')
    x, y = int(x), int(y)
    coordinates.append((x, y))

rows, _ = max(coordinates, key=lambda x: x[0])
_, cols = max(coordinates, key=lambda x: x[1])

# Add a border to the grid
rows += 1
cols += 1

# Create the grid
grid = [[-2 for _ in range(cols)] for _ in range(rows)]

area = 0
for i in range(rows):
    for j in range(cols):
        distance = 0
        for c in coordinates:
            distance += get_distance((i, j), c)
        if distance < 10000:
            area += 1

print(area)
