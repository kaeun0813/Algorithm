import heapq, sys
input=sys.stdin.readline
n=int(input())
array=[]
for i in range(n):
    array.append(list(map(int,input().split())))
array.sort(key=lambda x:x[0])

heap=[]
heapq.heappush(heap,array[0][1])
for i in range(1,n):
    if heap[0]<=array[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap,array[i][1])

print(len(heap))