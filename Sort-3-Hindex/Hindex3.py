def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0


# citations = [9, 8, 8, 8, 8]
citations = [4, 10, 20, 30, 40]
# citations = [9, 8, 8, 8, 8, 1, 1, 1, 1, 1]
# citations = [3, 0, 6, 1, 5]
# citations = [3, 3, 3, 3, 3]

# return = 3
result = solution(citations)
print(result)
