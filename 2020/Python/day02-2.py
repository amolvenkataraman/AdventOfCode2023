f = open("input2.txt", "r")

passwords = [i.rstrip() for i in f]
passwords1 = []
for i in passwords:
    i_ = i.split(" ")
    temp = [int(i_[0].split("-")[0]), int(i_[0].split("-")[1]), i_[1].split(":")[0], i_[2]]
    passwords1.append(temp)

ans = 0
for i in passwords1:
    letter = i[2]
    password_ = i[3]
    temp = 0
    if password_[i[0] - 1] == letter:
        temp += 1
    if password_[i[1] - 1] == letter:
        temp += 1

    if temp == 1:
        ans += 1

print(ans)

f.close()