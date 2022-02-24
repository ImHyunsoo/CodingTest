import random
import time


'''
airport_num이 500이면 오래 걸리고 
1000 이상이면 재귀 깊이 제한 오류 발생
제한 깊이 제한을 느슨하게 하거나 스택 자료 구조를 이용한 반복문 활용 가능
제일 느림..

dfs 활용
방문 처리 활용
dfs진행하면서 path와 방문 리스트를 업데이트함 (얕은 복사 주의)
전역 paths 2차원 배열 활용
'''

paths = []


def dfs(path, tickets, used_ticket):
    if False in used_ticket:          # 사용하지 않은 티겟이 있다면 함수 게속 진행
        # 다음 티겟 찾기
        for i, ticket in enumerate(tickets):
            next_path = path[:]                 # path값을 유지하기 위하여 next_path에 복사
            # used_tickek 값을 유지하기 위하여 next_used_ticket에 복사
            next_used_ticket = used_ticket[:]
            if path[-1] == ticket[0]:            # 다음 도착지를 가진 티겟을 발견하면
                if next_used_ticket[i] == False:   # 사용되지 않은 티겟임을 확인하고
                    # 다음 도착지를 next_path에 추가
                    next_path.append(ticket[1])
                    next_used_ticket[i] = True                # 그 티겟은 사용 처리함
                    # 경로와 티겟 사용여부 리스트를 업데이트하여 dfs에 넘김
                    dfs(next_path, tickets, next_used_ticket)
    else:            # 모든 티켓을 사용했다면  paths에 path를 추가하고 리턴
        paths.append(path)


def solution(tickets):
    global paths
    used_ticket = [False] * len(tickets)

    path = ["ICN"]  # path ICN 추가
    dfs(path, tickets, used_ticket)  # dfs 탐색 시작
    paths = sorted(paths)    # paths를 알파펫 순으로 정렬
    print(paths)

    return paths[0]   # 알파벳 순서가 가장 앞서는 경로를 리턴


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
