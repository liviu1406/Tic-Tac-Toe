text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]

n = int(input())
list = []

for i in text:
    for j in i:
        if len(j) <= n:
            # print(j)
            list.append(j)
print(list)


