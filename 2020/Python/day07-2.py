f = open("input7.txt", "r")

input_ = [i.rstrip().rstrip('.').split("contain") for i in f]

input1 = {}
for i in input_:
    input1[i[0].replace("bags", "").replace("bag", "").rstrip()] = [[] if a.lstrip().rstrip() == 'no other bags' else [int(a.lstrip().split(" ")[0]), ''.join([b for b in a.replace("bags", "").replace("bag", "") if not b.isdigit()]).lstrip().rstrip()] for a in i[1].split(',')]

def check_bags(type_):
    try:
        return sum([i[0] * (check_bags(i[1]) + 1) for i in input1[type_]])
    except IndexError:
        return 0

print(check_bags('shiny gold'))
