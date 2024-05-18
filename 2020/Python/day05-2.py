f = open("input5.txt", "r")

input_ = [i.rstrip() for i in f]

f.close()

ans = []
for i in input_:
    temp = i[0:7]
    a = 0
    for j in range(7):
        if temp[j] == "B":
            a += 2 ** (6 - j)
    
    temp = i[7:10]
    a1 = 0
    for j in range(3):
        if temp[j] == "R":
            a1 += 2 ** (2 - j)
    temp1 = (8 * a) + a1
    ans.append(temp1)

ans = sorted(ans)
ans1 = [ans[i+1] - ans[i] for i in range(len(ans)-1)]

for i in range(len(ans1)):
    if ans1[i] != 1:
        print(ans[i] + 1)