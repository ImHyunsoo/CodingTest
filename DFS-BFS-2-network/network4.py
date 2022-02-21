import random
import time

'''
방문하지 않았다면 방문함

BFS 
큐에 해당 노드 추가
방문처리함
해당 노드에 연결된 네트워크 있고, 그 연결된 노드를 방문하지 않았다면
방문 처리하고 큐에 연결된 노드를 추가

내 코드 n = 200 기, 속도 비슷함
'''


def solution(n, computers):
    def BFS(node, visit):
        que = [node]  # 큐에 해당 노드 추가
        visit[node] = 1  # 방문처리함
        while que:
            v = que.pop(0)  # 큐 (값 복사 일어나면서 시간 지연됨..)
            for i in range(n):
                # 해당 노드에 연결된 네트워크 있고, 그 연결된 노드를 방문하지 않았다면
                if computers[v][i] == 1 and visit[i] == 0:
                    visit[i] = 1    # 방문 처리하고
                    que.append(i)   # 큐에 연결된 노드를 추가
        return visit

    visit = [0 for i in range(n)]
    answer = 0
    for i in range(n):
        try:
            # 방문하지 않았다면 방문함, index(값), visit에서 해당 값을 가지는 인덱스 반환
            visit = BFS(visit.index(0), visit)
            answer += 1
        except:
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
