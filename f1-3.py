def solve(heads,legs):
    chicken_count=0
    rabbit_count=0
    rabbit_count=(legs-2*heads)/2
    chicken_count=heads-rabbit_count
    print(int(chicken_count),int(rabbit_count))
solve(35,94)