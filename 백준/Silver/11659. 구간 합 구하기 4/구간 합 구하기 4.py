n,m=map(int,input().split())

array=list(map(int,input().split()))
num=[]
for i in range(m):
    num.append(list(map(int,input().split())))
d=[0]*100001
d[0]=0
d[1]=array[0]
for i in range(2,n+1):
    d[i]=d[i-1]+array[i-1]
for i in range(m):
    print(d[num[i][1]]-d[num[i][0]-1])