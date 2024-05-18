inp = [10,16,6,0,1,17]

turn = 6
nums = inp
last = {}

for i in range(len(inp)):
    last[inp[i]] = i + 1


while True:
    num = nums[-1]
    turn += 1

    try:
        ind = last[num]
        nums.append(turn - ind)
        last[num] = turn
    except KeyError:
        nums.append(0)
        last[0] = turn
    
    if turn == 2020:
        print(nums)
        print(nums[-1])
        raise SystemExit