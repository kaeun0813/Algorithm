n= int(input()) #도시 개수
length=list(map(int,input().split())) # 도시 사이 간의 도로 길이 list
price=list(map(int,input().split())) # 각 도시마다 기름 값 list

total=0 #최소 비용

for i in range(n-1):
    if i ==0: #일단 출발을 하려면 처음 도시에서 기름을 무조건 넣어야 한다. 
        total+=price[i]*length[i]
        continue
    if price[i] <price[i-1]:# 이전 도시의 기름이 더 싸면 그 도시에서 기름 채우기
        total+=price[i]*length[i]
    else: # 이전 도시의 기름이 더 싸면 그 도시에서 기름 채우기
        total+=price[i-1]*length[i]
print(total)



