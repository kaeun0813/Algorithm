import sys
input = sys.stdin.readline
n=int(input())
array=[]
for i in range(n):
    array.append(list(map(int,input().split())))
d=[0]*(n+1)
for i in range(n-1,-1,-1):
    time=array[i][0]
    pay=array[i][1]
    if i+time<=n:
        d[i]=max(pay+d[i+time],d[i+1])
    else:
        d[i]=d[i+1]
print(d[0])