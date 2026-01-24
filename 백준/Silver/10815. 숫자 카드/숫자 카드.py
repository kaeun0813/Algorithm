n=int(input())
num=set(map(int,input().split()))
m=int(input())
array=list(map(int,input().split()))

for i in array:
    if i in num:
        print(1,end=" ")
    else:
        print(0, end=" ")
