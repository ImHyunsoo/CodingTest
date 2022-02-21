import random
import time

'''
코드가 2배 빠르고 간결함
dfs 방법 
방문한 노드의 연결 노드를 방문해서 방문처리함
방문하지 않은 노드 카운트하고 방문함
주석 참고
'''


def visit(k, graph, visited):
    visited[k] = 1                                  # 방문 처리함
    for i in range(len(graph[k])):                  # 해당 노드의 네트워크에 대하여
        if visited[i] == 0 and graph[k][i] == 1:    # 연결되고 방문하지 않은 노드가 있다면
            visit(i, graph, visited)                # 방문함


def solution(n, computers):

    visited = [0] * n

    answer = 0

    for i in range(n):
        if visited[i] == 0:                 # 방문하지 않았다면
            visit(i, computers, visited)    # 방문하고 카운트함
            answer += 1
        if 0 not in visited:                # 다 방문했다면  break
            break

    return answer


n = random.randint(1, 200)  # 컴퓨터의 개수 n은 1 이상 200 이하인 자연수
n = 200

visited = [[False] * n for _ in range(n)]
# print(visited)

# 연결에 대한 정보가 담긴 2차원 배열 computers
computers = []
for i in range(n):
    computer = []
    for j in range(n):
        if visited[i][j] == 0:           # 방문 하지 않았다면,
            if i == j:                       # 자신 자신과는 1로 표시하고, 방문처리
                computer.append(1)
            else:                            # 다른 컴터와는 0과 1 중에서 랜덤으로 표시하고, 두 컴터 간에는 방문처리
                computer.append(random.randint(0, 1))
            visited[i][j] = 1
            visited[j][i] = 1
        else:                            # 방문 했었다면, 그 연결 정보 표시
            computer.append(computers[j][i])
    computers.append(computer)
#     print(computer)
#     print(visited)
# print(computers)

start_time = time.time()
result = solution(n, computers)
print("--- %s seconds ---" % (time.time() - start_time))
print(result)
