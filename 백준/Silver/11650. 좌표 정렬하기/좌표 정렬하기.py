n=int(input())
array=[]
for i in range(n):
    array.append(list(map(int,input().split())))
array.sort(key=lambda x:(x[0],x[1]))
for i in range(n):
    print(array[i][0], array[i][1])