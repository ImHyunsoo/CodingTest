import random
import time

'''
각 노드 값 0 ~ n-1 으로 마킹함, i노드의 마킹값과 같은 마킹 값을 가진 노드들을,  연결된 j 노드의 마킹 값으로 업데이트함
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 0 0 0    0 0 0
[1, 1, 2, 3, 4, 5, 6, 7, 8, 9] 0 1 0    1 1 1
[1, 1, 2, 3, 4, 5, 6, 7, 8, 9] 0 1 1    1 1 1
[2, 1, 2, 3, 4, 5, 6, 7, 8, 9] 0 2 0    2 2 2
[2, 1, 2, 3, 4, 5, 6, 7, 8, 9] 0 2 2    2 2 2
[3, 1, 2, 3, 4, 5, 6, 7, 8, 9] 0 3 0    3 3 3
[3, 1, 2, 3, 4, 5, 6, 7, 8, 9] 0 3 3    3 3 3
[4, 1, 2, 3, 4, 5, 6, 7, 8, 9] 0 4 0    4 4 4
[4, 1, 2, 3, 4, 5, 6, 7, 8, 9] 0 4 4    4 4 4
[8, 1, 2, 3, 4, 5, 6, 7, 8, 9] 0 8 0    8 8 8
[8, 1, 2, 3, 4, 5, 6, 7, 8, 9] 0 8 8    8 8 8
[9, 1, 2, 3, 4, 5, 6, 7, 8, 9] 0 9 0    9 9 9
[9, 1, 2, 3, 4, 5, 6, 7, 8, 9] 0 9 9    9 9 9
[9, 9, 2, 3, 4, 5, 6, 7, 8, 9] 1 0 1    9 9 9
[9, 9, 2, 3, 4, 5, 6, 7, 8, 9] 1 0 9    9 9 9
[9, 9, 2, 3, 4, 5, 6, 7, 8, 9] 1 1 0    9 9 9
[9, 9, 2, 3, 4, 5, 6, 7, 8, 9] 1 1 1    9 9 9
[9, 9, 2, 3, 4, 5, 6, 7, 8, 9] 1 1 9    9 9 9
[3, 9, 2, 3, 4, 5, 6, 7, 8, 9] 1 3 0    9 3 3
[3, 3, 2, 3, 4, 5, 6, 7, 8, 9] 1 3 1    3 3 3
[3, 3, 2, 3, 4, 5, 6, 7, 8, 9] 1 3 3    3 3 3
[4, 3, 2, 3, 4, 5, 6, 7, 8, 9] 1 4 0    3 4 4
내 코드 n = 200 기준, 100배 이상 느림

같은 네트워크에 있는 노드는 같은 숫자로 치환시키는 과정인것같네요.. 근데 n이 커지면 나중에 시간복잡도가 n^2이라 ㅠ
플루이드-워셜 알고리즘을 이용한 것 같습니다. 궁금하시면 찾아보시면 좋을 것 같아요!
'''


def solution(n, computers):
    temp = []
    for i in range(n):
        temp.append(i)
    for i in range(n):               # 차례대로 0 ~ n-1 노드에 대해
        for j in range(n):
            if computers[i][j]:       # 네트워크가 존재한다면 (i와 연결된 j)
                for k in range(n):
                    # 각 노드 값 0 ~ n-1 으로 마킹함, i노드의 마킹값과 같은 마킹 값을 가진 노드들을,  연결된 j 노드의 마킹 값으로 업데이트함
                    if temp[k] == temp[i]:
                        temp[k] = temp[j]
                        # print(temp, i, j, k, '  ', temp[i], temp[j], temp[k])
    return len(set(temp))


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
