import random
import time
from collections import defaultdict

'''
chageword4.py의 깔끔한 버전

'''


def nextWord(cur, words):
    ret = []
    for word in words:
        if sum([word[i] != cur[i] for i in range(len(word))]) == 1:
            ret.append(word)
    return ret


def bfs(begin, target, words):
    visited = defaultdict(lambda: False)
    queue = nextWord(begin, words)
    level = 0

    while(len(queue) > 0):
        size = len(queue)
        level += 1

        for _ in range(size):
            key = queue.pop(0)
            visited[key] = True
            if (key == target):
                return level
            for candidate in nextWord(key, words):
                if (visited[candidate] == False):
                    queue.append(candidate)

    return 0


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
