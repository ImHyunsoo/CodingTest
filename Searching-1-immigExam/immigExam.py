def solution(n, times):
    answer = 0
    start = min(times)
    end = n * max(times)
    # mid == clock
    while start <= end:
        mid = (start + end)//2
        total = 0
        for time in times:
            total += mid // time
        if total >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    return answer


n = int(input())
times = list(map(int, input().split()))

# n = 6
# times = [7, 10]
# return 28

result = solution(n, times)
print(result)
