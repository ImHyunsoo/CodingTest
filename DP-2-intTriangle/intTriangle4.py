# 꼭대기가 누적된 합으로 최종 값 반환
# 피라미드 젤 밑에서 부터 위로 더해 올라감
def solution(triangle):

    height = len(triangle)

    while height > 1:
        for i in range(height - 1):
            triangle[height -
                     2][i] += max([triangle[height-1][i], triangle[height-1][i+1]])
        height -= 1

    answer = triangle[0][0]
    return answer
