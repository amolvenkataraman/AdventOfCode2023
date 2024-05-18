inp = [10,16,6,0,1,17]

turn = 6

nums = inp

while True:
    num = nums[-1]
    try:
        ind = list(reversed(nums[:-1])).index(num)
        nums.append(ind + 1)
    except ValueError:
        nums.append(0)
    
    turn += 1
    if turn == 2020:
        print(nums)
        print(nums[-1])
        raise SystemExit