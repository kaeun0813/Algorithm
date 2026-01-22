n=int(input())
array=[]
for i in range(n):
    data=input().split()
    array.append((int(data[0]),data[1]))
array.sort(key=lambda x:x[0])
for i in range(n):
    print(array[i][0],array[i][1])