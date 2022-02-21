import random
import time
from collections import deque as queue

'''
두 단어에 대해 한 글자만 다르면 True 리턴하는 함수 간결하게 구현, (zip, 컴프리헨션)
큐로 구현 (단어, 단계 카운트)
words의 각 단어마다 다음 단계 노드들을  사전에 추가 {단어, (담 단계 노드들)}
단어 갯수보다 단계 카운트가 크면 못찾은거니까 0 리턴 ( ->, <- 반복으로 큐 안 빌 수 있음을 방지)
해당 노드와 연결된 다음 단계 노드들에 대해서 타겟과 같으면 단계 카운트 값을 리턴함
다음 단계 노드들을 큐에 추가함 
'''


def transistable(a, b): return sum((1 if x != y else 0)       # 두 단어를 비교하여 한 글자만 다르면 True 리턴
                                   for x, y in zip(a, b)) == 1


def solution(begin, target, words):
    q, d = queue(), dict()    # 큐와 사전 초기화
    q.append((begin, 0))      # 큐에 단어와 카운트 값 넣음
    # 첫 노드와 연결된 다음 단계 노드들, 해당 단어를 키값으로  다음 단계노드들을 set 밸류로 사전 추가
    d[begin] = set(filter(lambda x: transistable(x, begin), words))
    for w in words:                                                 # 각 단어마다
        # 다음 단계 노드들을 위와같이 사전에 추가
        d[w] = set(filter(lambda x: transistable(x, w), words))
    while q:
        cur, level = q.popleft()    # 큐에서 해당 노드와 단계 카운트값 불러옴
        if level > len(words):     # 단어 갯수보다 단계 카운트가 크면 못찾은거니까 리턴 0
            return 0
        for w in d[cur]:            # 해당 노드와 연결된 다음 단계 노드들에 대해서
            if w == target:         # 타겟과 같으면  단계 카운트 값을 리턴함
                return level + 1
            else:
                q.append((w, level + 1))   # 다음 단계 노드들을 큐에 추가함
    else:
        return 0


len_word = random.randint(3, 10)  # 각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같음
words_num = random.randint(3, 50)  # words에는 3 ~ 50 개 단어가 있으며 중복 없음
words_num = 50
print("len_word: ", len_word)

# 각 단어는 길이가 모두 같고 알파벳 소문자로 구성됨 (26개 아스키 97 ~ 122)
# begin 만들기
begin = ""
for _ in range(len_word):
    begin += chr(random.randint(97, 122))
print("begin: ", begin)

# target 만들기 (단, begin과 같으면 안됨)
target = ""
while True:
    for _ in range(len_word):
        target += chr(random.randint(97, 122))
    if target != begin:
        break
print("target: ", target)

# words 만들기, 중복되는 단어 없음
words = []
cnt = 0
while True:
    word = ""
    for _ in range(len_word):
        word += chr(random.randint(97, 122))
    # print(len_word, word)
    if word in words:  # 단어가 중복되면 다시 단어 생성함
        continue
    words.append(word)
    cnt += 1
    if cnt == words_num:
        break
print(words_num, words)

# begin = "hit"
# target = "cog"
# words = ["hot", "dot", "dog", "lot", "log", "cog"]


# 실행 시간 및 결과 보기
start_time = time.time()
result = solution(begin, target, words)
print("--- %s seconds ---" % (time.time() - start_time))
print(result)
