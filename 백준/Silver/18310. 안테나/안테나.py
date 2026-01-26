n=int(input())
array=list(map(int,input().split()))
array.sort()
total1=0
total2=0
if len(array)%2!=0:
    print(array[n//2])
else:
    for i in range(n):
        total1+=abs(array[i]-array[n//2-1])
        total2+=abs(array[i]-array[n//2])
    if total1<=total2:
        print(array[n//2-1])
    else:
        print(array[n//2])
