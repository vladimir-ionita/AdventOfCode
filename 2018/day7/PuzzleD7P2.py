from utilities import FileUtilities
import collections
import string


input_file_path = "puzzle.in"
S = FileUtilities.get_sanitized_content_from_file(input_file_path)

alpha = string.ascii_uppercase
workers_max = 5
time_per_step = 60

steps = collections.defaultdict(list)
for i in S:
    s = i[5]
    d = i[36]
    steps[d].append(s)
    steps[s]


steps = collections.OrderedDict(sorted(steps.items()))

workers = collections.defaultdict(int)
time = 0
while steps or workers:
    jobs_done = []
    if workers:
        time += 1
    for k, v in workers.items():
        workers[k] -= 1
        if workers[k] == 0:
            jobs_done.append(k)
            for k1, v1 in steps.items():
                if k in v1:
                    steps[k1].remove(k)
            continue

    for j in jobs_done:
        workers.pop(j)

    jobs_ready = list({k for k, v in steps.items() if len(v) == 0})
    jobs_ready.sort()
    idle_workers = workers_max - len(workers)
    max_jobs = min(idle_workers, len(jobs_ready))

    for _ in range(max_jobs):
        next_job = jobs_ready[0]
        workers[next_job] = time_per_step + alpha.index(next_job) + 1
        jobs_ready.remove(next_job)
        steps.pop(next_job)

print(time)
