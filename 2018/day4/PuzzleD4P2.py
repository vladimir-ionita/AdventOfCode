from utilities import FileUtilities
from datetime import datetime
import collections

input_file_path = "puzzle.in"
file_input = FileUtilities.get_sanitized_content_from_file(input_file_path)


timeline = []
for i in file_input:
    timestamp = i[1:17]
    instruction = i[19:]

    date = datetime.strptime(timestamp, '%Y-%m-%d %H:%M')
    timeline.append((date, instruction))

t_ordered = sorted(timeline, key=lambda tup: tup[0])

sleep = collections.defaultdict(int)
g = 0
s_start = None
s_end = None
for k, v in t_ordered:
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



minute_max = 0
g_max = 0
for k, v in sleep.items():
    m_v = max(v)
    if minute_max < m_v:
        minute_max = m_v
        g_max = k


print(g_max, sleep[g_max].index(minute_max))
print(g_max * sleep[g_max].index(minute_max))
