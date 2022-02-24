import random
import time


'''
default dict라는 거 배워갑니다~! dfs 호출 전에 각 dfs 호출마다 가져야하는 footprint 같은 애들도 원래는 list copy를 이용했는데, 
호출 전후로 pop, insert 함으로써 한 리스트를 이용하는 좀 더 스택과 dfs 스러운 방법을 한 번 더 익힐 수 있었네요 ㅎㅎ 감사합니다

속도 향상
(list copy -> 호출 전후로 pop, insert 함으로써 한 리스트를 이용) 

default dict 및 정렬을 이용해서
각 출발지에 대한 도착지 리스트를 차례대로 가짐 

제귀 깊이 제한 997 
속도 개선 되었지만 여전히 느리고 재귀 깊이 제한 문제가 있음

 깊은 곳 리턴을 계속 이어 받아 리턴함
 
 알파벳 순으로 다음 나라를 찾으면 티켓츠에서 제거하고 패쓰에 추가
 반복을 거치며 dfs 탐색 중 죽을건 죽고 마지막 경로까지 완성한 dfs는 패쓰를 리턴
 리턴 받은 것을 고대로 받아서 쭉쭉 리턴
 
 길 가다가 막히면 dfs 빈거로 나온 후 티켓츠 원래대로 되돌리고 반복문 돌며 다음 dfs 탐색함
 못찾으면 이전 dfs로 가서 반복 
'''

from collections import defaultdict


def dfs(graph, N, key, footprint):
    # print(footprint)

    if len(footprint) == N + 1:   # 모든 경로를 거치면 footprint 리턴
        return footprint

    for idx, country in enumerate(graph[key]):  # 해당 출발지에 맞는 티겟의 도착지 나라들 [반복]
        graph[key].pop(idx)  # ["   "] : (pop)[] [] []   (도착지 나라들 하나씩 pop)

        tmp = footprint[:]       # 여기서 깊은 복사에 해당
        tmp.append(country)      # footprint에 티켓츠에서 pop한 나라를 추가

        # dfs 진행 (graph pop한거 업데이트, N 그대로, 새로운 출발지 나라, footprint 업데이트)
        ret = dfs(graph, N, country, tmp)
        # dfs 통해 각 경로를 만들어 나감
        # 깊이 우선 탐색에 초점하여 하나의 경로를 살펴보면, graph[key] = [] 되고 footprint는 늘어남,

        # 재귀가 소멸하는 과정에서는 pop해서 비었던 graph[key] = []이 다시 원래 대로 채워짐
        graph[key].insert(idx, country)
        # 다른 경로가 구축될 때, pop으로 빠졌던 graph[key] 를 원래대로 추가하는 효과 있음

        if ret:
            return ret                     # 경로가 중간에 끊기면 ret이 비어져버림
            # ['ICN', 'ATL', 'ICN', 'SFO', 'ATL', 'SFO'] 깊은 곳 리턴을 계속 이어 받아 리턴함
            # 맨 처음 dfs 만 수행..


def solution(tickets):
    answer = []

    graph = defaultdict(list)

    # ["ICN"] : (정렬) [] [] []
    # ["   "] :  []
    # ["   "] :  [] []
    # ...     : ...
    N = len(tickets)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
        graph[ticket[0]].sort()

    # answer = dfs(graph, N, "ICN", ["ICN"])
    answer = dfs(graph, N, "a", ["a"])

    return answer


airport_num = random.randint(3, 10000)  # 주어진 공항 수는 3개 이상 10,000개 이하
# airport_num = 500  # 996까지는 괜춘, 997 부터 재귀 깊이 제한 걸림
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
