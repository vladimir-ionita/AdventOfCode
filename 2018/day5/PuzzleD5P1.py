S = open('puzzle.in').read().strip()

stack = []
for c in S:
    if stack:
        last = stack[-1]
        if c.lower() == last.lower():
            if (c.isupper() and last.islower()) or (c.islower() and last.isupper()):
                stack.pop()
                continue
    stack.append(c)

print(len(stack))
