import random
import time


'''
travelPath3.py 와 비슷
간결하게 다시 코드 작성한 듯


알파벳 순으로 다음꺼 찾으면 티켓츠에서는 제거하고 스택에 쌓음
못찾으면 스택에서 빼서 path에 넣음
'''

from collections import defaultdict


def solution(tickets):
    r = defaultdict(list)
    for i, j in tickets:
        r[i].append(j)
    for i in r.keys():
        r[i].sort()

    # s = ["ICN"]
    s = ["a"]
    p = []
    while s:
        q = s[-1]
        if r[q] != []:
            s.append(r[q].pop(0))
        else:
            p.append(s.pop())
    return p[::-1]


airport_num = random.randint(3, 10000)  # 주어진 공항 수는 3개 이상 10,000개 이하
# airport_num = 10000
tickets = []
fr = "ICN"
for _ in range(airport_num):
    to = ""
    for _ in range(3):
        to += chr(random.randint(65, 90))  # A(65) ~ Z(90)
    ticket = [fr, to]      # [출발, 도착] 티켓
    fr = to
    tickets.append(ticket)  # 티켓 리스트
random.shuffle(tickets)  # 티켓 리스트 셔플
# print(tickets)

# tickets = [["ICN", "SFO"], ["ICN", "ATL"], [
#     "SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
tickets = [['a', 'g'], ['g', 'h'], ['h', 'i'], ['i', 'j'], [
    'j', 'e'], ['e', 'f'], ['a', 'w'], ['w', 'a']]

start_time = time.time()
result = solution(tickets)
print("--- %s seconds ---" % (time.time() - start_time))
print(result)
