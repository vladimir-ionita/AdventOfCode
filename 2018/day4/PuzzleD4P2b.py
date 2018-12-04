from utilities import FileUtilities
import collections

input_file_path = "puzzle.in"
file_input = FileUtilities.get_sanitized_content_from_file(input_file_path)

file_input = sorted(file_input)

C = collections.defaultdict(lambda: [0 for _ in range(60)])
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

        t_sleep = C[g]
        for i in range(t_start, t_end):
            t_sleep[i] += 1
        C[g] = t_sleep


minute_max = 0
g_max = 0
for k, v in C.items():
    m_v = max(v)
    if minute_max < m_v:
        minute_max = m_v
        g_max = k


print(g_max, C[g_max].index(minute_max))
print(g_max * C[g_max].index(minute_max))
