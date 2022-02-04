# -*- coding: utf-8 -*-
# # a b c d e f g h i j k l m n o p q r s t u v w x y z
# 조이스틱
import random
import time
import math

def solution(name):
    answer = 0
    
    # 상하 알파벳 바꾸기 카운트
    for c in name:
        u = ord(c) - ord('A')
        d = ord('Z') - ord(c) + 1
        answer += min(u, d)
    print("answer: ", answer)
    
    
    # 커서 이동 카운트
    m = len(name) - 1
    for i in range(len(name)):
        if name[i] == 'A':
            while idx < len(name) and name[idx] == 'A':
                idx += 1
            right = len(name) - idx
            left = 0 if i==0 else i-1
            turn = right + left + min(left, right)     
            m = min(m, turn)      # min(straight, return)
    answer += m
    print("answer: ", answer)

    return answer


name = ""
n = random.randint(1, 20)        # 글자 수는 1~20 중에서 랜덤하게 뽑힘
for _ in range(n):
    name += chr(random.randint(65, 90))   # 대문자 알파벳 문자열에 추가하기
print(name)

start_time = time.time()     

result = solution(name)

end_time = time.time()
time_duartion = end_time - start_time
print("time_duartion: ", time_duartion)
