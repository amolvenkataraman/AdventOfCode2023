f = [i for i in open("input13.txt", "r")]

timestamp = int(f[0])
buses = [i for i in f[1].rstrip().split(",") if i != 'x']

t = timestamp

while True:
    for i in buses:
        if t % int(i) == 0:
            print((t - timestamp) * int(i))
            raise SystemExit
    
    t += 1
