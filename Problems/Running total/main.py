n = [int(x) for x in input()]
print([sum(n[:x]) for x in range(1, len(n) + 1)])
