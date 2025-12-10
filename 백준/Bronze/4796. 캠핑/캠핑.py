#L,P,V순으로 입력받는다.
i=0
while True:
    l,p,v=list(map(int,input().split()))
    if l==0 and p == 0 and v==0:
        break
    i+=1
    if v%p<=l:
        print(f"Case {i}:",v//p*l+v%p)
    else:
        print(f"Case {i}:",v//p*l+l)
#v일짜리 휴가 중에서 임의의 연속한 p일을 고르더라도 캠핑장을 사용하는 기간이 L을 넘지 않아야 함.
#즉, v%p<=l이어야 함. 