import copy

f = open("input10.txt", "r")

input_ = [int(i.rstrip()) for i in f]
f.close()

input_.append(0)
input_.append(max(input_) + 3)
input_.sort()

options = [0 for i in range(len(input_))]
options[0] = 1
for i in range(len(input_)):
    for j in range(1, 4):
        if input_[i] + j in input_:
            options[i + j] += options[i]

print(options[-1])