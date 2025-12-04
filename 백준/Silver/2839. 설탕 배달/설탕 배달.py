n=int(input()) #배달해야 하는 설탕 무게
count=0

#5kg 먼저 최대한 쓰기
while n>=0:
    if n%5==0:
        count+=n//5
        print(count)
        break
    n-=3
    count+=1
else:
    print(-1)

