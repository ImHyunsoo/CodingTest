import random
import time
from collections import defaultdict

'''
bfs
해당 단어와 words들의 단어를 비교하여 한 글자만 다른 단어들을 리턴
해당 단계의 큐 사이즈 저장해서 사이즈만큼만 반복 돌면 단계별로 나누고 카운트 가능함
from collections import defaultdict
사전에 해당 키값이 없으면  키의 값이 False를 갖도록 추가
해당 단어를 방문처리
다음 단어를 방문하지 않았다면 방문함

깔끔한 버전 chageword6.py
'''


def nextWord(cur, words):  # 해당 단어와 words들의 단어를 비교하여 한 글자만 다른 단어들을 리턴
    ret = []
    for word in words:
        cnt = 0
        for idx in range(len(word)):
            if word[idx] == cur[idx]:
                cnt += 1
        if cnt == len(cur)-1:
            ret.append(word)
    return ret


def bfs(begin, target, words):
    # 사전에 해당 키값이 없으면  키의 값이 False를 갖도록 추가
    visited = defaultdict(lambda: False)
    queue = nextWord(begin, words)
    count = 0
    min = 1e9

    while(len(queue) > 0):  # 큐 빌때 까지 반복
        size = len(queue)  # 해당 단계의 큐 사이즈 저장
        count += 1         # 단계 별로 카운트

        for _ in range(size):   # 위 사이즈 만큼 큐의 단어들을 한 단어씩 반복
            key = queue.pop(0)   # 큐 동작이나 복사 시간 들 듯, deque 이용하자
            visited[key] = True    # 단어를 방문처리
            if (key == target and count < min):    # 타켓과 같으면 카운트 값 업데이트
                min = count
            # 해당 단어와 한 글자씩 다른 다음 단계 단어들 중에서 반복
            for candidate in nextWord(key, words):
                if (visited[candidate] == False):   # 다음 단어를 방문하지 않았다면 방문함
                    queue.append(candidate)

    if min == 1e9:
        return 0
    else:
        return min


def solution(begin, target, words):
    answer = bfs(begin, target, words)
    return answer


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
