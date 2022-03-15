import heapq
INF = int(1e9)


def solution(n, edge):
    # 거리 테이블 초기화
    distance = [INF] * (n+1)
    distance[1] = 0

    graph = [[] for _ in range(n+1)]
    # 간선 업데이트
    for a, b in edge:
        graph[a].append((b, 1))
        graph[b].append((a, 1))

    q = []
    start = 1
    heapq.heappush(q, (distance[1], start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for v, cost in graph[now]:
            if distance[now] + cost < distance[v]:
                distance[v] = distance[now] + cost
                heapq.heappush(q, (distance[v], v))

    max_dist = 0
    for i in range(1, n+1):
        if distance[i] == INF:
            continue
        if max_dist < distance[i]:
            max_dist = distance[i]

    return distance.count(max_dist)


n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
# return 3

print(solution(n, edge))
