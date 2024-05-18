f = open("input1.txt", "r")

nums = [int(i.rstrip()) for i in f]
f.close()

for i in nums:
    for j in nums:
        if i + j == 2020:
            print(i * j)