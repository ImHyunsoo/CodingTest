from collections import defaultdict


def DFS(G, IO, V, i, BASE):
    V[i] = True
    if i != BASE:
        IO[BASE][1] += 1
        IO[i][0] += 1
    for x in G[i]:
        if not V[x]:
            DFS(G, IO, V, x, BASE)


def solution(n, results):
    G = [[] for _ in range(n+1)]
    IO = defaultdict(lambda: [0, 0])
    answer = 0

    for a, b in results:
        G[a].append(b)

    for i in range(1, n+1):
        DFS(G, IO, [False] * (n+1), i, i)

    for i in range(1, n+1):
        if IO[i][0] + IO[i][1] == n - 1:
            answer += 1

    return answer


print(solution(6, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5], [2, 6]]))
