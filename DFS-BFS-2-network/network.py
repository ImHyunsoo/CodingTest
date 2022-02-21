import random
import time

'''
0  >>  1 1 0
1  >>  1 1 1
2  >>  0 1 1
============
0  >>  1 1 0
1  >>  1 1 0
2  >>  0 0 1

음료수 붓기  # 물 붓기 아님.. 네트워크..
1. 특정 노드로 방문하고 주변 상, 하, 좌, 우를 살편본 뒤 주변 지점 중에서 값이 '1'이면서, 아직 방문하지 않은 지점이 있다면 해당지점을 방문함
2. 방문한 지점에서 주변을 살펴보면서 방문을 진행하는 과정을 반복하면, 연결된 모든 지점을 방문할 수 있음
3. 모든 노드에 대하여 1~2 번 과정을 반복하며, 방문하지 않은 지점의 수를 카운트함 
'''

'''
네트워크
1. 특정 노드로 방문하고 연결된 노드를 살펴본 뒤 연결노드 중에서 값이 '1'이면서, 아직 방문하지 않은 노드가 있다면 해당 노드를 방문함
2. 방문한 지점에서 연결 노드를 살펴보면서 방문을 진행하는 과정을 반복하면, 연결된 모든 지점을 방문할 수 있음
3. 모든 노드에 대하여 1~2 번 과정을 반복하며, 방문하지 않은 지점의 수를 카운트함 
'''

# 특정 노드로 방문하고 연결된 모든 노드 방문함


def dfs(computers, v, visited2):
    # 방문 하지 않았다면, 방문 처리,
    if visited2[v] == False:
        visited2[v] = True

        # 해당 노드에 네트워크가 존재한다면
        b_net = False
        for j in range(len(computers)):
            if computers[v][j] == 1:
                b_net = True
                if not visited2[j]:  # 연결된 노드를 방문하지 않았다면 그 노드를 방문함
                    dfs(computers, j, visited2)
        if b_net == True:  # 방문하지 않았고 네트워크가 존재한다면 True
            return True
    # 해당 노드를 방문 했었다면 False
    return False


def solution(n, computers):
    answer = 0
    visited2 = [False] * n  # 방문 리스트, False로 초기화

    for v in range(n):      # 0 ~ n-1 모든 노드에 대해
        # 노드에 방문함,
        # 해당 노드를 방문 했었다면 False,
        # 방문하지 않았고 네트워크가 존재했다면 True
        if dfs(computers, v, visited2) == True:
            answer += 1
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
