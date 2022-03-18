INF = int(1e9)


def solution(n, results):
    answer = 0
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        graph[i][i] = 0

    for a, b in results:
        graph[a][b] = 1
        graph[b][a] = -1

    for i in range(1, n + 1):
        for k in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1
                    graph[j][i] = 1
                elif graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                    graph[j][i] = -1

    for g_list in graph:
        cnt = 0
        for g in g_list:
            if g == 1 or g == -1:
                cnt += 1
        if cnt == n-1:
            answer += 1

    return answer


# n = 5
# results = [[1, 2], [4, 5], [3, 4], [2, 3]]
# n = 6
# results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5], [2, 6]]
n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
# return 2

print(solution(n, results))
