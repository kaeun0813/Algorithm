import sys
input=sys.stdin.readline
n=int(input())
i=j=1
if n==1:
    print(1)
else:
    while True:
        if i>=n:
            break
        i+=j*6
        j+=1
    print(j)