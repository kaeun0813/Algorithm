x=int(input())

count=x-2
# 1. 재귀 방식의 실행 횟수 (피보나치 수의 값과 동일함)
# 실제 재귀를 돌리면 시간 초과가 나므로, DP로 구한 값으로 대체합니다.
f=[0]*41
def fibonacci(x):
    f[1]=1
    f[2]=1
    
    for i in range(3,x+1):
        f[i]=f[i-1]+f[i-2]
    return f[x]
# 2. 반복문 방식의 실행 횟수
# 3부터 n까지 루프를 돌므로 n - 2 번 실행됨
print(fibonacci(x),count)    