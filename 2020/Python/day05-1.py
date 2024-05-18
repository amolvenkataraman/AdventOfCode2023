f = open("input5.txt", "r")

input_ = [i.rstrip() for i in f]

f.close()

ans = 0
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
    if temp1 > ans:
        ans = temp1

print(ans)