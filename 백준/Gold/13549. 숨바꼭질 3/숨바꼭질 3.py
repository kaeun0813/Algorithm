import sys, heapq
input = sys.stdin.readline

INF = 10**15
MAX = 100000

n, k = map(int, input().split())

def dijkstra(start):
    distance = [INF] * (MAX + 1)
    q = []
    heapq.heappush(q, (0, start))  # (시간, 위치)
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        if now == k:
            return dist

        for nx, w in ((now * 2, 0), (now - 1, 1), (now + 1, 1)):
            if 0 <= nx <= MAX:
                nt = dist + w
                if nt < distance[nx]:
                    distance[nx] = nt
                    heapq.heappush(q, (nt, nx))

    return distance[k]

print(dijkstra(n))
