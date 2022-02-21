import random
import time

'''
zip을 이용해서 한 글자씩 비교 
방문한 단어는 words 에서 단어 삭제
해당 단계의 노드들과 다음 단계의 노드들을 처리
다음 단계로 갈 때 ++1 카운트
'''


def solution(begin, target, words):
    answer = 0
    Q = [begin]

    while True:
        temp_Q = []
        for word_1 in Q:             # 한 단어씩 반복       # Q는 한 단계씩 밝고 있는 단계별 노드들임
            if word_1 == target:     # 단어와 타켓이 같다면 answer 리턴
                return answer
            for i in range(len(words)-1, -1, -1):  # 마지막 단어 부터  첫 단어까지 반복
                word_2 = words[i]
                if sum([x != y for x, y in zip(word_1, word_2)]) == 1:  # 한 글자만 다른 단어라면
                    # words에서 삭제하고 temp_Q에 추가  # temp_Q 는 다음 단계 노드들임
                    temp_Q.append(words.pop(i))

        if not temp_Q:      # temp_Q가 비어있으면 0 리턴
            return 0
        Q = temp_Q
        answer += 1


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
