N=int(input())
P=list(map(int,input().split()))

P.sort()
total=0
for x in range(1,N+1):
    total+=sum(P[0:x])
print(total)
