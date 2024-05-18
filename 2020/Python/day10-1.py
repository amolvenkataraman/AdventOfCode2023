import copy

f = open("input10.txt", "r")

input_ = [int(i.rstrip()) for i in f]
f.close()

input_.append(0)
input_.append(max(input_) + 3)
input_.sort()

diffs = [input_[i + 1] - input_[i] for i in range(len(input_) - 1)]

ans = diffs.count(1) * diffs.count(3)

print(ans)