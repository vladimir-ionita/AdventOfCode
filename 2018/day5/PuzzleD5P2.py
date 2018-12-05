import string

S = open('puzzle.in').read().strip()
alphabet = string.ascii_lowercase

pol_len = []
for l in alphabet:
    S_filtered = S.replace(l, '').replace(l.upper(), '')

    stack = []
    for c in S_filtered:
        if stack:
            last = stack[-1]
            if c.lower() == last.lower():
                if (c.isupper() and last.islower()) or (c.islower() and last.isupper()):
                    stack.pop()
                    continue
        stack.append(c)
    pol_len.append(len(stack))

print(min(pol_len))
