import math
test_count=int(input())
for i in range(test_count):
    a,b=map(int, input().split())
    print(math.lcm(a,b))
    
