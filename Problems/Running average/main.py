number = input()
int_list = [int(x) for x in number]
print([(int_list[x] + int_list[x + 1]) / 2 for x in range(4)])

