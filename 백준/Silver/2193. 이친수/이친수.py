#n 자리 수까지 무조건 1로 시작
n=int(input())
d=[0]*91
d[1]=1
d[2]=1
for i in range(3,n+1):
    d[i]=d[i-1]+d[i-2]
print(d[n])