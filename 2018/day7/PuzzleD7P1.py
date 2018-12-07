from utilities import FileUtilities
import collections


input_file_path = "puzzle.in"
S = FileUtilities.get_sanitized_content_from_file(input_file_path)

steps = collections.defaultdict(list)
for i in S:
    s = i[5]
    d = i[36]
    steps[d].append(s)
    steps[s]


steps = collections.OrderedDict(sorted(steps.items()))
steps_traveled = []
while steps:
    steps_ready = list({k for k, v in steps.items() if len(v) == 0})
    steps_ready.sort()
    next_step = steps_ready[0]
    steps_traveled.append(next_step)

    for k, v in steps.items():
        if next_step in v:
            steps[k].remove(next_step)

    steps.pop(next_step)

print(''.join(steps_traveled))
