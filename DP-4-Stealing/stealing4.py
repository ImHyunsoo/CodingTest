# 처음 코드 개선
def solution(m):
    d1 = [0] * len(m)
    d2 = [0] * len(m)
    d1[0] = d1[1] = m[0]
    d2[1] = m[1]
    for i in range(2, len(m)):
        d1[i] = max(d1[i - 1], d1[i - 2] + m[i])
        d2[i] = max(d2[i - 1], d2[i - 2] + m[i])
    return max(d1[-2], d2[-1])


# return 4
# print(solution([1, 2, 3000000, 1]))
# print(solution([1, 2, 3, 1]))
print(solution([10, 2, 2, 100, 2]))
