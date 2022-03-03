import random
import time


'''
알파벳이 앞선 다음 도착지로 이동 및 스택에 추가 
제일 빠름 
재귀 깊이 제한도 문제 없음
dfs 아닌 스택 반복문 이용

알파벳 순으로 다음꺼 찾으면 티켓츠에서 제거하고 스택에 쌓음
못찾으면 스택에서 제거하고 패쓰에 추가함
'''


def solution(tickets):
    routes = {}           # 빈 사전
    for t in tickets:
        # key = 출발지, values = 도착지 리스트
        # .get(a, []),  a 키값이 없을 시 default로 [], 그렇지 않으면 키에 맞는 밸류값을 반환
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    for r in routes:
        routes[r].sort(reverse=True)        # 도착지 리스트를 내림차순 정렬
    stack = ["ICN"]
    path = []
    while len(stack) > 0:
        top = stack[-1]
        # 다음 도착지로 연결될 티켓이 없거나 티켓을 다 사용해서 못쓰는 경우
        if top not in routes or len(routes[top]) == 0:
            # 스택에서 그 경로를 뺌, 다른 길을 찾기 위함 (해당 길이 막히면 한칸 뒤로가서 다른 길 찾아나감, 반복)
            path.append(stack.pop())
            # path에 추가함 (거꾸로 맨 도착지부터 출발지로 차례대로 path에 추가)
            # 중간 경로가 끊긴다는 건 그 지점이 마지막으로 가야한다는 걸 의미함
        else:
            stack.append(routes[top][-1])   # 알파벳 순서가 앞선 도착지를 스택에 넣고
            routes[top] = routes[top][:-1]  # 도착 리스트에서 제외함
    return path[::-1]


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

tickets = [["ICN", "SFO"], ["ICN", "ATL"], [
    "SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]


start_time = time.time()
result = solution(tickets)
print("--- %s seconds ---" % (time.time() - start_time))
print(result)
