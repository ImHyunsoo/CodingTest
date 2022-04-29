from collections import deque

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(board, x, y):
    n = len(board)
    in_direction = [[set() for _ in range(n)]
                    for _ in range(n)]  # 노드로 들어온 방향을 저장하는 배열
    in_direction[0][0] = {0, 2}  # 원점에서는 들어온 방향을 상(0), 좌(2)로 설정
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 벽인 경우 무시
            if board[nx][ny] == 1:
                continue
            # 상하좌우 이동에 따라 수평이동인지, 수직이동인지 확인하기 위한 변수 설정
            if i < 2:
                a, b, c, d = 0, 1, 2, 3
            else:
                a, b, c, d = 2, 3, 0, 1
            # 현재노드로 들어온 방향과 다음 노드로 들어가는 방향이 수평이라면 직선도로만 건설
            if a in in_direction[x][y] or b in in_direction[x][y]:
                # 다음 노드가 더 적은 비용으로 업데이트 가능하다면 들어가는 방향을 클리어
                if board[nx][ny] > board[x][y] + 100:
                    in_direction[nx][ny].clear()
                # 다음 노드가 한번도 업데이트 되지 않앗거나 같거나 더 적은 비용으로 건설 가능하면 업데이트
                if board[nx][ny] == 0 or board[nx][ny] >= board[x][y] + 100:
                    board[nx][ny] = board[x][y] + 100
                    in_direction[nx][ny].add(i)  # 다음 노드로 들어가는 방향을 업데이트
                    queue.append((nx, ny))

            # 현재노드로 들어온 방향과 다음 노드로 들어가는 방향이 수직이라면 직선도로, 코너 건설
            elif c in in_direction[x][y] or d in in_direction[x][y]:
                # 다음 노드가 더 적은 비용으로 업데이트 가능하다면 들어가는 방향을 클리어
                if board[nx][ny] > board[x][y] + 100 + 500:
                    in_direction[nx][ny].clear()
                # 다음 노드가 한번도 업데이트 되지 않았거나 같거나 더 적은 비용으로 건설 가능하면 업데이트
                if board[nx][ny] == 0 or board[nx][ny] >= board[x][y] + 100 + 500:
                    board[nx][ny] = board[x][y] + 100 + 500
                    in_direction[nx][ny].add(i)  # 다음 노드로 들어가는 방향을 업데이트
                    queue.append((nx, ny))

    # 가장 오른쪽 아래까지의 경주로 건설 최소 비용 반환
    return board[n-1][n-1]
