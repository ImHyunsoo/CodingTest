import random
import time

'''
dfs
한 글자만 다른 단어면 True 반환하는 함수
타겟과 같으면 카운트 리턴함
words를 줄여나가는데 비면, dfs 죽임 return
words의 단어들을 반복 
  각 단어에 대해 해당 노드와 비교하여 다음 단계 노드들을 찾음
  그 단어는 words에서 제외하고 다음 dfs 호출(단계 카운트 업데이트))
'''

answer = 0


def solution(begin, target, words):

    dfs(begin, target, 0, words)
    return answer


def change(fr, to):                              # 두 단어를 비교
    for i in range(len(fr)):
        if fr[:i]+fr[i+1:] == to[:i]+to[i+1:]:  # 한 글자씩 빼고 같으면 True 리턴
            return True
    return False


def dfs(begin, target, d, words):
    global answer
    # print(begin)
    # print(words)
    if begin == target:    # 타켓과 같으면 카운트 리턴함
        # print(d)
        answer = d
        return
    else:
        if len(words) == 0:   # words 빈거면 리턴
            return
        for w in range(len(words)):           # 각 단어의 인덱스
            if change(begin, words[w]):       # 두 단어를 비교함, 한 글자만 다르다면 True
                # words에서 한 글자만 달랐던 단어만 빼고 word에 저장함
                word = words[:w]+words[w+1:]
                # 해당 단어, 타겟, 단계 카운트 처리, words 업데이트
                dfs(words[w], target, d+1, word)


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
