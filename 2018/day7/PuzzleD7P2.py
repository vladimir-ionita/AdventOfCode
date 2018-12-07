from utilities import FileUtilities
import collections
import string


input_file_path = "puzzle.in"
S = FileUtilities.get_sanitized_content_from_file(input_file_path)

alpha = string.ascii_uppercase
workers_max = 5
time_per_step = 60

M = collections.defaultdict(list)
letters = set()
for i in S:
    s = i[5]
    d = i[36]
    M[d].append(s)
    M[s]


M = collections.OrderedDict(sorted(M.items()))

W = collections.defaultdict(int)
time = 0
while len(M.keys()) != 0 or len(W.keys()) != 0:
    jobs_done = []
    if len(W.items()) != 0:
        time += 1
    for k, v in W.items():
        W[k] -= 1
        if W[k] == 0:
            jobs_done.append(k)
            for k1, v1 in M.items():
                if k in v1:
                    M[k1].remove(k)
            continue

    for j in jobs_done:
        W.pop(j)

    jobs = list({k for k, v in M.items() if len(v) == 0})
    jobs.sort()
    idle_workers = workers_max - len(W.keys())
    max_jobs = min(idle_workers, len(jobs))

    for _ in range(max_jobs):
        j = jobs[0]
        W[j] = time_per_step + alpha.index(j) + 1
        jobs.remove(j)
        M.pop(j)


print(time)
