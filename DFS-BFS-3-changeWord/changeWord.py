import random
import time
from collections import deque

'''
1. 한 글자만 다른 단어 찾기 및 방문
2. 그 단어에서 또 다시 한 글자만 다른 단어 찾고 방문하지 않았다면 방문하기 
3. 위 과정으로 모든 한 글자만 다른 단어의 연결을 찾을 수 있음
4. 정답 찾으면 최솟값, 못 찾으면 0 

1. 한 글자만 다른 단어 찾기
>> 앞에서 끝까지 한 글자씩 비교하기 
(시간 오래 걸릴 듯- 모든 단어에 대해 한 글자씩 모두 비교해야 하기 때문)

>> 정렬? 놉 안됨


>> find() 한 글자 뺀 단어를 찾는다? 
abcdk  놉 안됨
akcdk

>> & 연산 이용하기? 놉 안됨  
01 비트에서나 되지 문자열에서는 안됨  
aa
ba  0 1 나와야 하는데 1 1 

>> 정규식 사용하여 python 문자열 비교
import re
복잡하기도 하지만 하나만 다른거 찾기 적용 안됨


>> difflib   놉 안됨
difflib의 SequenceMatcher를 사용해서 두 개의 문자열의 유사성을 수치화
abcd
dabc  0 나와야 하는데 0.75  

>> substring 이용하기 가능성 있음
abcdefdef
abikefdef
인덱스 조절해가며 문자열 자르기 
if x in str 앞 뒤로 확인하기


===>> 하나씩 접근해서 비교하기 vs substring으로 부분 문자열 비교하기 
결과 모름 
쉬운거로 가자 [하나씩 접근해서 비교하기]
'''

'''
> 방문처리
> 카운트 처리 하기
> target에 도달 했는지 체크

맨처음에 방문 처리 한다면
    dfs로 인해 방문 처리된 노드가 있다면 dfs를 거쳤기 때문에 최소값일 수 없음 
    따라서 방문 처리가 된 노드를 방문해야 최소값 됨
    그말은 방문 처리하면 안된다
    
해당 노드에서  한글자 차이 나는 노드를 찾고 이전에 방문했던 노드가 아니라면 방문함

bfs로 바꾸고 (카운터 처리 편할거 같은 느낌)
최대 words 수 50 보다 카운트 커지는데도 정답 못찾으면 0 리턴
'''
visited = [False] * 50
step = [0] * 51


def bfs(begin, target, words):
    queue = deque()
    queue.append((-1, begin))   # 맨처음 begin의 인덱스는 -1 로 처리

    while queue:
        idx, temp = queue.popleft()

        if temp == target:      # 정답을 맞춤
            return step[idx]    # 스탭 카운트 리턴

        # 한 글자 다른 단어 찾기
        for i, word in enumerate(words):
            wrong_cnt = 0
            for j in range(len(word)):
                if word[j] != temp[j]:
                    wrong_cnt += 1            # 한 글자씩 틀릴 때마다 카운트
                if wrong_cnt > 1:             # 두 글자 이상 틀리면 다음 단어 비교
                    break

            # 한 글자만 틀리고 방문한적 없으면 방문함
            if wrong_cnt == 1 and visited[i] == False:
                visited[i] = True
                step[i] = step[idx] + 1       # 노드에 대해 단계를 밟을 때마다 카운트
                queue.append((i, word))       # 큐에 인덱스와 노드 추가

    return 0


def solution(begin, target, words):
    if not target in words:   # target이 words 없으면 변환이 불가능하므로 0 리턴
        print("target이 words에 없음")
        return 0
    if begin in words:    # begin이 words에 있으면 words에서 begin을 제거
        # words에 중복 없으므로 remove(), 중복 있었다면 remove_set과 컴프리헨션 이용
        words.remove(begin)
    return bfs(begin, target, words)  # bfs


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
