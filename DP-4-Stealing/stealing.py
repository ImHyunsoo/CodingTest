def solution(m):
    d1 = [0] * len(m)
    d1[0] = m[0]
    d1[1] = 0
    d1[2] = max(d1[1], d1[0] + m[2])
    for i in range(3, len(m)):
        d1[i] = max(d1[i-1], d1[i-2] + m[i], d1[i-3] + m[i])
    print(d1)

    d2 = [0] * len(m)
    d2[0] = 0
    d2[1] = m[1]
    d2[2] = max(d2[1], d2[0] + m[2])
    for i in range(3, len(m)):
        d2[i] = max(d2[i-1], d2[i-2] + m[i], d2[i-3] + m[i])
    print(d2)

    return max(d1[-2], d2[-1])


# return 4
# print(solution([1, 2, 3000000, 1]))
print(solution([1, 2, 3, 1]))
# print(solution([10, 2, 2, 100, 2]))
# print(solution([1, 2, 3]))
