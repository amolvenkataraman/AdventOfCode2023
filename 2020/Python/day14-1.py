f = [i.rstrip().split(" = ") for i in open("input14.txt", "r")]

mask = ""
mem = {}

def masked(num):
    num1 = str(bin(num).replace("0b", ""))
    num1 = "".join(["0" for i in range(len(mask) - len(num1))]) + num1
    
    ans = []    
    for i in range(len(num1)):
        if mask[i] == 'X':
            ans.append(num1[i])
        else:
            ans.append(mask[i])

    return int("".join(ans), 2)

for i in f:
    if i[0] == "mask":
        mask = i[1]
    else:
        mem[i[0].split("[")[1].split("]")[0]] = masked(int(i[1]))

print(sum(mem[i] for i in mem))