from itertools import product
import copy

f = [i.rstrip().split(" = ") for i in open("input14.txt", "r")]

mask = ""
mem = {}

def masked(num):
    num1 = str(bin(num).replace("0b", ""))
    num1 = "".join(["0" for i in range(len(mask) - len(num1))]) + num1
    
    ans = []
    for i in range(len(num1)):
        if mask[i] == '0':
            ans.append(num1[i])
        else:
            ans.append(mask[i])
    
    ans1 = []

    for p in product([0, 1], repeat=ans.count('X')):
        temp = copy.deepcopy(ans)
        a = 0
        for i in range(len(ans)):
            if ans[i] == 'X':
                temp[i] = str(p[a])
                a += 1
            else:
                pass

        ans1.append(int("".join(temp), 2))

    return ans1

for i in f:
    if i[0] == "mask":
        mask = i[1]
    else:
        for i_ in masked(int(i[0].split("[")[1].split("]")[0])):
            mem[i_] = int(i[1])


print(sum(mem[i] for i in mem))