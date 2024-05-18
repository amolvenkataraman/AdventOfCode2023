f = open("input8.txt", "r")

input_ = [i.rstrip().split(" ") for i in f]

executed = []
acc = 0
pos = 0
while True:
    if pos in executed:
        break
    else:
        executed.append(pos)
    
    temp = input_[pos]
    if temp[0] == 'jmp':
        pos += int(temp[1])
    elif temp[0] == 'acc':
        acc += int(temp[1])
        pos += 1
    else:
        pos += 1

print(acc)