from itertools import permutations

f = [i.rstrip() for i in open("input16.txt", "r")]
f.append('')

f1 = []
temp = []

for i in f:
    if i == '':
        f1.append(temp)
        temp = []
    else:
        temp.append(i)

numbers = [i.split(": ") for i in f1[0]]
myticket = f1[1][1].split(',')
othertickets = [i.split(',') for i in f1[2][1:]]

fields = [[a[i] for a in othertickets] for i in range(len(myticket))]
fields1 = []

ans = 0

for ticket in othertickets:
    for field in ticket:
        valid = False
        for number in numbers:
            constraints = number[1].split(" or ")
            if (int(field) >= int(constraints[0].split("-")[0]) and int(field) <= int(constraints[0].split("-")[1])) or (int(field) >= int(constraints[1].split("-")[0]) and int(field) <= int(constraints[1].split("-")[1])):
                valid = True
        
        if valid == False:
            ans += int(field)

print(ans)

for i in range(len(fields)):
    best = -1
    best1 = -1
    best2 = 100000000
    for j in range(len(numbers)):
        temp = 0
        constraints = numbers[j][1].split(" or ")
        
        for k in fields[i]:
            if (int(k) >= int(constraints[0].split("-")[0]) and int(k) <= int(constraints[0].split("-")[1])) or (int(k) >= int(constraints[1].split("-")[0]) and int(k) <= int(constraints[1].split("-")[1])):
                temp += 1

        if temp > best1 or (temp == best1 and (int(constraints[0].split("-")[1]) - int(constraints[0].split("-")[0])) + (int(constraints[1].split("-")[1]) - int(constraints[1].split("-")[0]))) < best2:
            best2 = (temp == best1 and (int(constraints[0].split("-")[1]) - int(constraints[0].split("-")[0])) + (int(constraints[1].split("-")[1]) - int(constraints[1].split("-")[0])))
            best1 = temp
            best = j

    fields1.append(best)

print([i[0] for i in numbers])
print(fields1)
