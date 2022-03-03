def solution(citations):
    citations.sort(reverse=True)
    n = len(citations)
    for k in range(n, -1, -1):
        paper = [citation for citation in citations if k <= citation]
        length = len(paper)
        if length >= k:
            return k


citations = [9, 8, 8, 8, 8]
# citations = [9, 8, 8, 8, 8, 1, 1, 1, 1, 1]
# citations = [3, 0, 6, 1, 5]
# citations = [3, 3, 3, 3, 3]

# return = 3
result = solution(citations)
print(result)
