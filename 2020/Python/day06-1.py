f = open("input6.txt", "r")

input_ = [i.rstrip() for i in f]
input_.append('')

f.close()

input1 = []
temp = ""
for i in range(len(input_)):
    if input_[i] == '':
        input1.append(temp)
        temp = ""
    else:
        for l in input_[i]:
            temp += l

ans = 0
for i in input1:
    ans += len(set(i))

print(ans)