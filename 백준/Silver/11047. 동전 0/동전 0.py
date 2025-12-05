#필요한 동전 개수의 최소값
#n은 동전 종류, k는 최종합
n,k= list(map(int,input().split()))
coins=[]
count=0

for i in range(n):
    coins.append(int(input()))# n만큼 동전종류 받기

coins.sort(reverse=True)

while k>0:
    for coin in coins:
        if k >= coin: #coin과 같거나 k가 더 큰 경우만
            count+=k//coin
            k%=coin
        
print(count)