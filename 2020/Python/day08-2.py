import copy

f = open("input8.txt", "r")

input_ = [i.rstrip().split(" ") for i in f]
inps = []

for i in range(len(input_)):
    if input_[i][0] == 'nop' or input_[i][0] == 'jmp':
        temp = copy.deepcopy(input_)
        temp1 = copy.deepcopy(temp[i][0])
        if temp1 == 'nop':
            temp[i][0] = 'jmp'
        elif temp1 == 'jmp':
            temp[i][0] = 'nop'
        inps.append(temp)

for input_ in inps:
    executed = []
    acc = 0
    pos = 0
    while True:
        if pos in executed:
            break
        else:
            executed.append(pos)
        
        if pos == len(input_):
            print(acc)
            raise SystemExit
        
        temp = input_[pos]
        if temp[0] == 'jmp':
            pos += int(temp[1])
        elif temp[0] == 'acc':
            acc += int(temp[1])
            pos += 1
        else:
            pos += 1
