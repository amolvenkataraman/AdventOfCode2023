f = open("input4.txt", "r")

input_ = [i.rstrip() for i in f]
input_.append('')

passports = []
temp = []
for i in input_:
    if i == '':
        passports.append(temp)
        temp = []
    else:
        for f in i.split(" "):
            temp.append(f)

ans = 0
for i in passports:
    temp = {f.split(":")[0]: f.split(":")[1] for f in i}
    
    if 'byr' in temp and 'iyr' in temp and 'eyr' in temp and 'hgt' in temp and 'hcl' in temp and 'ecl' in temp and 'pid' in temp:
        ans += 1

print(ans)

"""
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
"""