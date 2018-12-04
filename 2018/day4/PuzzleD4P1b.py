from utilities import FileUtilities
import collections

input_file_path = "puzzle.in"
file_input = FileUtilities.get_sanitized_content_from_file(input_file_path)

# Sort
file_input = sorted(file_input)


sleep = collections.defaultdict(int)
g = 0
t_start = None
for t in file_input:
    op = t[19:]
    if op.startswith("Guard"):
        g = op.split()[1]
        g = int(g[1:])
    if op.startswith("falls"):
        t_start = t[15:17]
        t_start = int(t_start)
    if op.startswith("wakes"):
        t_end = t[15:17]
        t_end = int(t_end)

        time_asleep = []
        if g in sleep:
            time_asleep = sleep[g]
        else:
            time_asleep = [0 for x in range(60)]

        for i in range(t_start, t_end):
            time_asleep[i] += 1
        sleep[g] = time_asleep

max = 0
g = 0
for k, v in sleep.items():
    if sum(v) > max:
        max = sum(v)
        g = k

ts = list(sleep[g])
max = 0
max_m = 0
for i in range(0, 60):
    if max < ts[i]:
        max = ts[i]
        max_m = i

print(max_m)
print(g*max_m)
