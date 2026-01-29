from collections import Counter
n=int(input())
array=[]
for i in range(n):
    array.append(int((input())))
counter=Counter(array)
max_freq=max(counter.values())
cadidates=[num for num, freq in counter.items() if freq==max_freq]
print(min(cadidates))