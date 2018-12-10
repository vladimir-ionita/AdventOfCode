from utilities import FileUtilities
import math


def get_coordinates_after_time(coordinates_velocities, time_in_seconds):
    coordinates = []
    for k, v in coordinates_velocities.items():
        c = (k[0] + time_in_seconds * v[0],
             k[1] + time_in_seconds * v[1])
        coordinates.append(c)
    return coordinates


input_file_path = "puzzle.in"
S = FileUtilities.get_sanitized_content_from_file(input_file_path)

# Parse input
M = {}
for l in S:
    coordinates = l[10:24]
    coordinates = coordinates.split(', ')
    x = int(coordinates[0])
    y = int(coordinates[1])

    velocity = l[36:42]
    velocity = velocity.split(', ')
    x_direction = int(velocity[0])
    y_direction = int(velocity[1])

    M[(x, y)] = (x_direction, y_direction)

# Find the smallest grid possible
grid_size = (math.inf, math.inf)
time = 0
while True:
    coordinates = get_coordinates_after_time(M, time)
    x_min, _ = min(coordinates, key=lambda x: x[0])
    x_max, _ = max(coordinates, key=lambda x: x[0])
    _, y_min = min(coordinates, key=lambda x: x[1])
    _, y_max = max(coordinates, key=lambda x: x[1])
    w = x_max - x_min
    h = y_max - y_min

    if w > grid_size[0] or h > grid_size[1]:
        time -= 1   # the last good result
        break

    grid_size = (w, h)
    time += 1

# Build the grid
print(time)
coordinates = get_coordinates_after_time(M, time)
x_min, _ = min(coordinates, key=lambda x: x[0])
x_max, _ = max(coordinates, key=lambda x: x[0])
_, y_min = min(coordinates, key=lambda x: x[1])
_, y_max = max(coordinates, key=lambda x: x[1])
w = x_max - x_min + 1   # +1 to include the last coordinate
h = y_max - y_min + 1   # +1 to include the last coordinate
print(w, h)

rows = h
cols = w
grid = [['.' for _ in range(cols)] for _ in range(rows)]
for c in coordinates:
    c_r = (c[1] - y_min, c[0] - x_min)
    grid[c_r[0]][c_r[1]] = '#'

# Print the grid
for i in range(h):
    print(''.join(grid[i]))
