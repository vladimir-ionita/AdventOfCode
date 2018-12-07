from utilities import FileUtilities
import collections


input_file_path = "puzzle.in"
S = FileUtilities.get_sanitized_content_from_file(input_file_path)

M = collections.defaultdict(list)
letters = set()
for i in S:
    s = i[5]
    d = i[36]
    M[d].append(s)
    M[s]


M = collections.OrderedDict(sorted(M.items()))

letters = []
while {k:v for k, v in M.items()}:
    empty = list({k for k, v in M.items() if len(v) == 0})
    empty.sort()
    empty_letter = empty[0] if empty else None
    letters.append(empty[0])

    for k, v in M.items():
        if empty_letter in v:
            M[k].remove(empty_letter)

    M.pop(empty_letter)

print(''.join(letters))
