f = open("input6.txt", "r")

input_ = [i.rstrip() for i in f]
input_.append('')

f.close()

input1 = []
input2 = []
temp = ""
temp1 = 0
for i in range(len(input_)):
    if input_[i] == '':
        input1.append(temp)
        input2.append(temp1)
        temp = ""
        temp1 = 0
    else:
        for l in input_[i]:
            temp += l
        temp1 += 1

ans = 0
for i in range(len(input1)):
    temp = {a: input1[i].count(a) for a in "".join(list(set(input1[i])))}
    for t in temp:
        if temp[t] == input2[i]:
            ans += 1

print(ans)