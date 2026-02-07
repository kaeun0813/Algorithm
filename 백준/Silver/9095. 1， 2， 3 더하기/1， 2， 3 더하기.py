t=int(input())
n=[]
for i in range(t):
    n.append(int(input()))
def fibo(x):
    d=[0]*10000001
    d[1]=1
    d[2]=2
    d[3]=4
    for i in range(4,x+1):
        d[i]=d[i-1]+d[i-2]+d[i-3]
    return d[x]

for num in n:
    print(fibo(num))


