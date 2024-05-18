import copy

f = open("input9.txt", "r")

input_ = [int(i.rstrip()) for i in f]
f.close()

for i in range(len(input_)):
    if i > 24:
        temp = False
        for j in range(i - 25, i):
            for k in range(i - 25, i):
                if input_[j] + input_[k] == input_[i]:
                    temp = True
        if temp == False:
            print(input_[i])
            raise SystemExit