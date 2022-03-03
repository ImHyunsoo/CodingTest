import random
import time


'''
내 코드와 유사한 방식 
그리고 유사한 성능
방문여부 리스트는 만들지 않음
path는 늘리고, ticList는 줄여나가며 업데이트
'''


def solution(tickets):
    answer = []

    def dfs(start, ticList, path):
        path.append(start)
        if len(ticList) == 1:
            path.append(ticList[0][1])
            answer.append(path)
            return
        for t in ticList:
            if t[0] == start:
                ticList_copy = ticList.copy()
                ticList_copy.remove(t)
                dfs(t[1], ticList_copy, path.copy())
    dfs("ICN", tickets, [])
    print(answer)
    return min(answer)


airport_num = random.randint(3, 10000)  # 주어진 공항 수는 3개 이상 10,000개 이하
# airport_num = 800
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

tickets = [["ICN", "SFO"], ["ICN", "ATL"], [
    "SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]


start_time = time.time()
result = solution(tickets)
print("--- %s seconds ---" % (time.time() - start_time))
# print(result)
