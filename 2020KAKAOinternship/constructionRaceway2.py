from collections import deque


def solution(board):
    INF = 1e+10
    n = len(board)
    # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 각 노드는 상하좌우 4개 방향을 가지고 있으며 각 방향은 최소 비용을 저장
    node_in_direction_cost = [[[INF] * 4 for _ in range(n)] for _ in range(n)]
    node_in_direction_cost[0][0] = [0, 0, 0, 0]  # 원점에서는 각 방향의 cost 0으로 설정
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((0, 0))
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 경주로 건설 부지를 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 벽인 경우 무시
            if board[nx][ny] == 1:
                continue
            # 상으로 나갈 시, 상으로 들어왔다면 + 100, 좌나 우로 들어왔다면 + 600, 하로 들어오지 못하므로 INF
            if i == 0:
                min_cost = min(node_in_direction_cost[x][y][0]+100, INF,
                               node_in_direction_cost[x][y][2]+600, node_in_direction_cost[x][y][3]+600)
            # 하로 나갈 시, 상으로 들어왔다면 INF, 좌나 우로 들어왔다면 + 600, 상로 들어오지 못하므로 INF
            elif i == 1:
                min_cost = min(
                    INF, node_in_direction_cost[x][y][1]+100, node_in_direction_cost[x][y][2]+600, node_in_direction_cost[x][y][3]+600)
            # 좌로 나갈 시, 상이나 하로 들어왔다면 +600, 좌로 들어왔다면 + 100, 우로 들어오지 못하므로 INF
            elif i == 2:
                min_cost = min(node_in_direction_cost[x][y][0]+600, node_in_direction_cost[x]
                               [y][1]+600, node_in_direction_cost[x][y][2]+100, INF)
            # 우로 나갈 시, 상이나 하로 들어왔다면 +600, 우로 들어왔다면 + 100, 좌로 들어오지 못하므로 INF
            elif i == 3:
                min_cost = min(node_in_direction_cost[x][y][0]+600, node_in_direction_cost[x]
                               [y][1]+600, INF, node_in_direction_cost[x][y][3]+100)

            # 해당 방향에서 들어오는 도로를 건설할 시 비용이 더 적게 들면 업데이트
            if node_in_direction_cost[nx][ny][i] > min_cost:
                node_in_direction_cost[nx][ny][i] = min_cost
                queue.append((nx, ny))
                for i in range(n):
                    for j in range(n):
                        print(
                            f'{min(node_in_direction_cost[i][j]):>13}', end=' ')
                    print()
                print()

    # 가장 오른쪽 아래에서 최솟값을 리턴
    return min(node_in_direction_cost[n-1][n-1])


# board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# # result 900

# board = [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [
#     0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]
# # # result 3800

# board = [[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]
# # result 2100

# board = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0],
#          [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]
# # result 3200

board = [[0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1], [
    1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0]]
# result 4500

result = solution(board)
print(result)


# https://unho94.tistory.com/m/130
# https://ckd2806.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B2%BD%EC%A3%BC%EB%A1%9C-%EA%B1%B4%EC%84%A4
# https://ojt90902.tistory.com/537
# https://programmers.co.kr/questions/21325
# https://programmers.co.kr/questions/17381
# https://programmers.co.kr/questions/11840
