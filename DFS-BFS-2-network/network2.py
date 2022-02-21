import random
import time

'''
1. solution 함수 안에 dfs함수를 정의하여 사용함 *
2. dfs 함수는 재귀를 쓰지 않고 스택으로 풀음 *
3. 해당 노드를 방문하지 않았다면 방문처리함
4. 해당 노드에 네트워크가 존재하고 연결된 노드가 방문되지 않았다면 방문함
5. 연결된 모든 노드에는 방문처리되고 방문 하지 않았던 첨 노드를 카운트함
내 코드 기준 50배 느림 *
visited[j] == 1인 경우에도 for문을 돌아가는데, 
if visited[j]: continue 를 추가 
1.5배 느림

'''


def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]

    def dfs(computers, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()
            if visited[j] == 1:  # 방문 했다면 continue
                continue
            visited[j] = 1    # 방문 처리함

            # for i in range(len(computers)-1, -1, -1):
            for i in range(0, len(computers)):
                # 해당 노드에 네트워크가 존재하고 연결된 노드를 방문하지 않았다면 방문함
                if computers[j][i] == 1 and visited[i] == 0:
                    stack.append(i)
    i = 0
    while 0 in visited:  # 모두 방문처리 될 때까지 반복함
        if visited[i] == 0:    # 방문하지 않은 노드를 방문함
            dfs(computers, visited, i)
            answer += 1
        i += 1
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
