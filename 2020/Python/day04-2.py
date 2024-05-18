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
        if ((len(temp['byr']) == 4 and int(temp['byr']) >= 1920 and int(temp['byr']) <= 2002) and
            (len(temp['iyr']) == 4 and int(temp['iyr']) >= 2010 and int(temp['iyr']) <= 2020) and
            (len(temp['eyr']) == 4 and int(temp['eyr']) >= 2020 and int(temp['eyr']) <= 2030)):
            if temp['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                if len(temp['pid']) == 9:
                    if len(temp['hcl']) == 7 and temp['hcl'][0] == '#':
                        if (temp['hgt'][-1] == 'm' and temp['hgt'][-2] == 'c') or (temp['hgt'][-1] == 'n' and temp['hgt'][-2] == 'i'):
                            valid = True
                            for l in temp['hcl'][1:]:
                                if l not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
                                    valid = False
                            if (temp['hgt'][-1] == 'm' and temp['hgt'][-2] == 'c'):
                                if not (int(temp['hgt'][:-2]) >= 150 and int(temp['hgt'][:-2]) <= 193):
                                    valid = False
                            else:
                                if not (int(temp['hgt'][:-2]) >= 59 and int(temp['hgt'][:-2]) <= 76):
                                    valid = False

                            if valid == True:
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