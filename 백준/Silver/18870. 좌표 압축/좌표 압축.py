n=int(input())
array=list(map(int,input().split()))

new=[]
new2=[]
for i in range(n):
    new.append((i,array[i]))
#(인덱스, 수)
new.sort(key=lambda x: x[1])
count=0
for i in range(n):
    if i==0:
        new2.append((new[i][0],count))
        count+=1
    else:
        if new[i][1]==new[i-1][1]:
            new2.append((new[i][0],count-1))
        else:
            new2.append((new[i][0],count))
            count+=1
new2.sort(key=lambda x: x[0])
for i in range(n):
    print(new2[i][1],end=' ')