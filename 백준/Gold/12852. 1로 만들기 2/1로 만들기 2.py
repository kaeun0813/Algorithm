n=int(input())
d=[0]*1000001
d[2]=1
d[3]=1
for i in range(4,n+1):
    d[i]=d[i-1]+1
    if i%2==0:
        d[i]=min(d[i],d[i//2]+1)
    if i%3==0:
        d[i]=min(d[i],d[i//3]+1)      
print(d[n])
curr=n
while True:
    print(curr,end=" ")
    if curr==1:
        break
    if d[curr]==d[curr-1]+1:
        curr=curr-1
    elif curr%2==0 and d[curr]==d[curr//2]+1:
        curr=curr//2
    elif curr%3==0 and d[curr]==d[curr//3]+1:
        curr=curr//3
    
