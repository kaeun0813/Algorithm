buget=int(input())
price=list(map(int,input().split()))

#각자의 자산
jun=buget
jun_stock=0
sung=buget
sung_stock=0

high=0
low=0

for i in range(14):
    #준현이의 경우
    if price[i]<=jun:
        jun_stock+=jun//price[i] #주식 수
        jun=jun%price[i] #남은 금액은 현재 금액으로 업데이트
        



    #성민이의 경우
    #3일 상승  -> 무조건 하락 (전량 매도) | 3일 하락-> 무조건 상승 (전량 매수)
    if i==0:
        next_num = price[0]
    elif next_num < price[i]: #이전 값이 작으면 (상승 판단)
        high+=1
        low=0
    elif next_num >price[i]: #이전 값이 큰면(하락 판단)
        low+=1
        high=0
    else:
        high=0
        low=0
    next_num=price[i]

    if low>=3:  #주식을 사야 함
        if sung>=price[i]:
            #print("주식 매입 가격",price[i])
            sung_stock+=sung//price[i]
            sung=sung%price[i]

    elif high>=3: #주식을 팔아야 함.
        if sung_stock>0:
            #print("주식 매도 가격",price[i])
            sung=sung_stock*price[i]
            sung_stock=0


if (jun+price[13]*jun_stock) <(sung+price[13]*sung_stock):
    print("TIMING")
elif (jun+price[13]*jun_stock) > (sung+price[13]*sung_stock):
    print("BNP")
else:
    print("SAMESAME")

#print(jun+price[13]*jun_stock, sung+price[13]*sung_stock)

