def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer


citations = [9, 8, 8, 8, 8]
# citations = [9, 8, 8, 8, 8, 1, 1, 1, 1, 1]
# citations = [3, 0, 6, 1, 5]
# citations = [3, 3, 3, 3, 3]

# return = 3
result = solution(citations)
print(result)
