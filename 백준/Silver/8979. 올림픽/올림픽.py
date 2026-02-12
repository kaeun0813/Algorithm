n,k=map(int,input().split())
array=[]
for i in range(n):
    array.append(list(map(int,input().split())))
array.sort(key=lambda x:(-x[1],-x[2],-x[3]))
rank=1
for i in range(n):
    if i>0 and (array[i][1],array[i][2],array[i][3])!=(array[i-1][1],array[i-1][2],array[i-1][3]):
        rank=i+1
    if array[i][0]==k:
        print(rank)
        break
