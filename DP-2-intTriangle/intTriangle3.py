# 상향식 탑다운 재귀
# 피라미드 밑에서 부터 합하여 올라가는 구조
# 꼭대기 값 반환
def solution(triangle):
    memo = {}
    answer = f(triangle, 0, 0, memo)
    return answer


def f(triangle, i, j, memo):
    if i == len(triangle)-1:
        return triangle[i][j]

    if (i, j) in memo:
        return memo[(i, j)]

    a = f(triangle, i+1, j, memo)
    b = f(triangle, i+1, j+1, memo)
    x = triangle[i][j] + max(a, b)

    memo[(i, j)] = x

    return x
