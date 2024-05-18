f = open("input7.txt", "r")

input_ = [i.rstrip().rstrip('.').split("contain") for i in f]

input1 = {}
for i in input_:
    input1[i[0].replace("bags", "").replace("bag", "").rstrip()] = [''.join([b for b in a.replace("bags", "").replace("bag", "") if not b.isdigit()]).lstrip().rstrip() for a in i[1].split(',')]

ans = []
def check_bags(type_):
    for i in input1:
        if type_ in input1[i]:
            if i not in ans:
                ans.append(i)
                check_bags(i)

check_bags('shiny gold')
print(len(ans))