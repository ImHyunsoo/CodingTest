# 보텀업
def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                left = -1
                right = triangle[i - 1][j]
            elif j == i:
                left = triangle[i - 1][j - 1]
                right = -1
            else:
                right = triangle[i - 1][j]
                left = triangle[i - 1][j - 1]
            triangle[i][j] = max(left, right) + triangle[i][j]
    max_value = -1
    for value in triangle[-1]:
        max_value = max(max_value, value)
    return max_value
