import random
import time

'''
enumerate 사용
내 코드 기준, 속도 비슷함
stack 처리
방문하지 않았고 연결되었다면 노드를 방문함
연결처리 후 방문 하지 않은 노드있다면 방문하고 카운함, 그리고 다시 연결처리 반복
'''


def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]                 # 방문 리스트 초기화

    while sum(visited) != n:                        # 모두 방문할 때까지 반복
        searching = [visited.index(0), ]            # 방문하지 않은 노드 방문하고 카운트
        answer += 1

        while searching:
            target_node = searching.pop()
            # 해당 노드와 연결된 노드의 연결여부와, 인덱스
            for node_num, connected in enumerate(computers[target_node]):
                if connected and not visited[node_num]:     # 방문하지 않았고 연결되었다면
                    visited[node_num] = 1           # 그 노드를 방문함
                    searching.append(node_num)

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
