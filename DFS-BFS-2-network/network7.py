import random
import time
from collections import deque

'''
from collections import deque 큐 처리
솔루션 함수 안에  
방문하지 않은 노드에 대해
    큐 구현
    해당 노드와 연결된 노드가 있고 그 노드가 방문되지 않았다면
    방문하고 카운트함
내 코드 기준 속도 비슷함
'''


def solution(n, computers):
    visited = {}
    answer = 0
    for i in range(n):
        if i in visited:
            continue   # 방문했었다면 continue
        answer += 1                   # 방문하지 않은 노드
        q = deque([i])                    # 카운트 및 큐에 해당 노드 추가
        visited[i] = True                 # 해당 노드 방문 처리
        while q:
            # node = q.pop()                # 이거 스택 아니냐고..
            node = q.popleft()
            for j in range(n):                          # 해당 노드의 네트워크에 대하여
                if node != j and computers[node][j] == 1:       # 연결되어 있는 노드에 대하여
                    if j not in visited:                        # 방문 하지 않은 노드라면
                        visited[j] = True                                 # 방문함
                        q.append(j)
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
