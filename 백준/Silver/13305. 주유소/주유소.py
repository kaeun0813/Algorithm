n= int(input()) #도시 개수
length=list(map(int,input().split())) # 도시 사이 간의 도로 길이 list
price=list(map(int,input().split())) # 각 도시마다 기름 값 list

total=0 #최소 비용
min_price=price[0]

for i in range(n-1):
    if price[i] < min_price:# 이전 도시의 기름이 더 싸면 그 도시 기름값으로 바꾸기       
        min_price=price[i]
    total+=min_price*length[i]

print(total)
