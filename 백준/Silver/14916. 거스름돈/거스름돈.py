#동전의 개수가 최소가 되도록 거슬러 주어야 함
money=int(input())
change=0
while True:
    while money>0:
        if money%5==0:
            break
        money-=2
        change+=1
    if money<=0:
        break
    money-=5
    change+=1
if money==0:
    print(change)
else:
    print(-1)   

