def solution(m, n, puddles):
    d = [[0] * m for _ in range(n)]
    for c, r in puddles:
        d[r-1][c-1] = -1
    for c in range(1, m):
        if d[0][c] != -1:
            d[0][c] = 1
        else:
            break
    for r in range(1, n):
        if d[r][0] != -1:
            d[r][0] = 1
        else:
            break
    for r in range(1, n):
        for c in range(1, m):
            if d[r][c] == -1:
                continue
            if d[r-1][c] == -1 and d[r][c-1] == -1:
                d[r][c] = 0
            elif d[r-1][c] == -1 and d[r][c-1] != -1:
                d[r][c] = d[r][c-1]
            elif d[r-1][c] != -1 and d[r][c-1] == -1:
                d[r][c] = d[r-1][c]
            else:
                d[r][c] = d[r-1][c] + d[r][c-1]
    return d[-1][-1] % 1000000007


print(solution(4, 3, [[2, 2]]))
# return 4
