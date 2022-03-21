from collections import defaultdict
import random
import sys
sys.setrecursionlimit(int(1e6))

# 런타임 에러 - 재귀 깊이 해제
# 윈도우에서는 1993까지.. 리눅스에서는 그 이상 되는 듯
# dfs 재귀 말고 반복문 사용해야지 싶다
vec = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
answer = 0
edges = defaultdict(set)


def DFS(x, y, idx, arrows):
    if idx == len(arrows):
        return
    global answer
    if arrows[idx] == 1 or arrows[idx] == 3 or arrows[idx] == 5 or arrows[idx] == 7:
        for _ in range(2):
            next_x = x + vec[arrows[idx]][0]/2
            next_y = y + vec[arrows[idx]][1]/2
            # ->, <- 왔던길 되돌아가는 경우
            if (next_x, next_y) in edges[(x, y)]:
                pass
            else:  # 이전에 방문 했던 노드인 경우
                if (next_x, next_y) in edges:
                    answer += 1
                edges[(x, y)].add((next_x, next_y))
                edges[(next_x, next_y)].add((x, y))
            x, y = next_x, next_y
    else:
        next_x = x + vec[arrows[idx]][0]
        next_y = y + vec[arrows[idx]][1]
        if (next_x, next_y) in edges[(x, y)]:
            pass
        else:
            if (next_x, next_y) in edges:
                answer += 1
        edges[(x, y)].add((next_x, next_y))
        edges[(next_x, next_y)].add((x, y))

    DFS(next_x, next_y, idx+1, arrows)


def solution(arrows):
    DFS(0, 0, 0, arrows)
    return answer


arrows = []
for i in range(10000):
    arrows.append(random.randint(0, 7))
# arrows = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]
# arrows = [6, 5, 2, 7, 1, 4, 2, 4, 6]
# arrows = [5, 2, 7, 1, 6, 3]
# arrows = [6, 2, 4, 0, 5, 0, 6, 4, 2, 4, 2, 0]
print(solution(arrows))
