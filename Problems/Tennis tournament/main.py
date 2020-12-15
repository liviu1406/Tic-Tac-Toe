name_list = [input().split() for i in range(int(input()))]
name_win = [i[0] for i in name_list for j in i if j == "win"]
print(f"{name_win}\n{len(name_win)}")