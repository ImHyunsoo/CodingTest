def solution(distance, rocks, n):
    answer = 0
    end = distance
    start = 0
    rocks.sort()
    rocks.append(end)
    while start <= end:
        mid = (start + end) // 2

        offset, cnt = 0, 0
        for rock in rocks:
            if rock - offset < mid:
                cnt += 1
            else:
                offset = rock
        if cnt > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
    return answer


distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2
# return 4

result = solution(distance, rocks, n)
print(result)
