import sys
input = sys.stdin.readline
n=int(input())
array=[]
for i in range(n):
    array.append(int(input()))
array.sort()
print(round(sum(array)/n))
print(array[n//2])

modes = []
max_freq = 0
current_freq = 1

for i in range(1, n):
    if array[i] == array[i - 1]:
        current_freq += 1
    else:
        if current_freq > max_freq:
            max_freq = current_freq
            modes = [array[i - 1]]
        elif current_freq == max_freq:
            modes.append(array[i - 1])
        current_freq = 1

# 마지막 숫자 처리
if current_freq > max_freq:
    modes = [array[-1]]
elif current_freq == max_freq:
    modes.append(array[-1])

modes.sort()

if len(modes) > 1:
    print(modes[1])
else:
    print(modes[0])
    
print(array[-1] - array[0])