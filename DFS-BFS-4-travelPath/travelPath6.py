import random
import time


'''
내 코드와 유사한 방식 
그리고 유사한 성능
'''

candidates = []


def visit(start, graph, visited, cnt, route):
    global candidates
    if cnt == len(graph):
        candidates.append(route.split(" "))
    else:
        for i in range(len(graph)):
            if visited[i] == 0 and graph[i][0] == start:
                go = []
                for j in range(len(visited)):
                    go.append(visited[j])
                go[i] = 1
                visit(graph[i][1], graph, go, cnt+1, route+" "+graph[i][1])


def solution(tickets):
    answer = []
    tickets.sort()
    visited = [0] * len(tickets)
    visit("ICN", tickets, visited, 0, "ICN")
    # print(candidates)
    return candidates[0]


airport_num = random.randint(3, 10000)  # 주어진 공항 수는 3개 이상 10,000개 이하
# airport_num = 500
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
