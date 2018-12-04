from utilities import FileUtilities
from datetime import datetime
import collections

input_file_path = "puzzle.in"
file_input = FileUtilities.get_sanitized_content_from_file(input_file_path)

# Sort
file_input = sorted(file_input)


timeline = []
for i in file_input:
    timestamp = i[1:17]
    instruction = i[19:]

    date = datetime.strptime(timestamp, '%Y-%m-%d %H:%M')
    timeline.append((date, instruction))

sleep = collections.defaultdict(int)
g = 0
s_start = None
s_end = None
for k, v in timeline:
    if v.startswith("Guard"):
        g = v.split()[1]
        g = int(g[1:])
    if v.startswith("falls"):
        if k.hour != 0:
            s_start = 0
        else:
            s_start = k.minute

    if v.startswith("wakes"):
        if k.hour != 0:
            s_end = 0
        else:
            s_end = k.minute

        time_asleep = []
        if g in sleep:
            time_asleep = sleep[g]
        else:
            time_asleep = [0 for x in range(60)]

        for i in range(s_start, s_end):
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
