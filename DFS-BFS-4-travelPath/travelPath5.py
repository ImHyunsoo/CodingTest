import random
import time


'''
재귀
tickets 줄이고, route 늘려나가며 업데이트하면서 진행 
정렬을 이용하여 알파벳이 앞선 경로를 바로 찾음 
티켓의 인덱스를 이용하여 문제를 풀어나감 
재귀 깊이 제한 문제 있음 997

알파벳 앞선 순으로 패쓰에 추가하며 업데이트
티켓츠에서는 패쓰에 추가한 티켓을 삭제
티켓츠가 다 비어지면 패쓰를 반환

none을 반환하면 이전 dfs에서 탐색하며 역시 none을 반환하면  더 이전 dfs로 이동함
이전으로 이동한 dfs 는 반복문 돌며 탐색하고 다음으로 진전 못하면 none을 반환하기를 반복함
'''


def solution(tickets):
    def helper(tickets, route):
        if tickets == []:
            return route
        left = [i for i in range(len(tickets)) if tickets[i][0] == route[-1]]
        if left == []:
            return None
        left.sort(key=lambda i: tickets[i][1])

        for next in left:
            rest = helper(tickets[:next]+tickets[next+1:],
                          route+[tickets[next][1]])
            if rest is not None:
                return rest
    # return helper(tickets, ["ICN"])
    return helper(tickets, ["a"])


airport_num = random.randint(3, 10000)  # 주어진 공항 수는 3개 이상 10,000개 이하
airport_num = 500
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

# tickets = {{"a", "g"}, {"g", "h"}, {"h", "i"}, {"i", "j"}, {"j", "e"}, {"e", "f"}, {"a", "w"}, {"w", "a"}};

tickets = [['a', 'g'], ['g', 'h'], ['h', 'i'], ['i', 'j'], [
    'j', 'e'], ['e', 'f'], ['a', 'w'], ['w', 'a']]

start_time = time.time()
result = solution(tickets)
print("--- %s seconds ---" % (time.time() - start_time))
# print(len(result))
print(result)
