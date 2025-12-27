#끝나는 시간이 짧은 순으로 정렬
n=int(input())
time=[]
count=0 #사용회의수
for i in range(n):
    time.append(list(map(int,input().split())))
time.sort(key=lambda x : (x[1],x[0]))

min_time=0
for i in range(n):
    if min_time <= int(time[i][0]):
        min_time=int(time[i][1])
        count+=1
print(count)