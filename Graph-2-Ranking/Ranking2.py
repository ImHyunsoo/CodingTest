from collections import defaultdict


def solution(n, results):
    answer = 0
    win_graph = defaultdict(set)    # 이긴 애들
    lose_graph = defaultdict(set)   # 진 애들

    for winner, loser in results:        # 결과에서 이기고 진 애들 그래프화
        win_graph[loser].add(winner)
        lose_graph[winner].add(loser)

    for i in range(1, n+1):
        # i한테 진 애들은 i를 이긴 애들한테도 진 것
        for winner in win_graph[i]:
            lose_graph[winner].update(lose_graph[i])
        # i한테 이긴 애들은 i한테 진 애들한테도 이긴 것
        for loser in lose_graph[i]:
            win_graph[loser].update(win_graph[i])

    for i in range(1, n+1):
        # i한테 이기고 진 애들 합쳐서 n-1이면 순위가 결정된 것
        if len(win_graph[i]) + len(lose_graph[i]) == n-1:
            answer += 1

    return answer


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
# return 2

print(solution(n, results))
