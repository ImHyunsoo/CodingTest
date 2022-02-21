import random
import time
from collections import deque

'''
        for c, w in zip(current, word):
            if c != w:
                count += 1
                
        yield        
        
        queue 
        
        노드와 카운트를 같이 딕셔너리로 저장함
'''


def get_adjacent(current, words):
    for word in words:
        if len(current) != len(word):
            continue

        count = 0
        for c, w in zip(current, word):  # 한 글자씩 비교하며 카운트
            if c != w:
                count += 1

        if count == 1:             # 한 글자만 다른 단어면 yield
            yield word


def solution(begin, target, words):
    dist = {begin: 0}        # 사전 자료형으로 단어와 단계 카운트 다음
    queue = deque([begin])

    while queue:
        current = queue.popleft()

        # next_word가 한 글자만 다른 단어를 받으면
        for next_word in get_adjacent(current, words):
            if next_word not in dist:
                dist[next_word] = dist[current] + \
                    1       # 딕셔너리 key와 value 값 추가
                queue.append(next_word)

    # 사전 key로 value 얻기,  (찾으려는 key 값이 없을 경우 미리 정해 둔
    return dist.get(target, 0)
    # 디폴트 값을 대신 가져오게 하고 싶을때, get(x, '디폴트 값') 사용함)


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
