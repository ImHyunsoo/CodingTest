# -*- coding: utf-8 -*-
# # a b c d e f g h i j k l m n o p q r s t u v w x y z
# ���̽�ƽ
import random
import time
import math

def solution(name):
    answer = 0
    
    # ���� ���ĺ� �ٲٱ� ī��Ʈ
    for c in name:
        u = ord(c) - ord('A')
        d = ord('Z') - ord(c) + 1
        answer += min(u, d)
    print("answer: ", answer)
    
    
    # Ŀ�� �̵� ī��Ʈ
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
n = random.randint(1, 20)        # ���� ���� 1~20 �߿��� �����ϰ� ����
for _ in range(n):
    name += chr(random.randint(65, 90))   # �빮�� ���ĺ� ���ڿ��� �߰��ϱ�
print(name)

start_time = time.time()     

result = solution(name)

end_time = time.time()
time_duartion = end_time - start_time
print("time_duartion: ", time_duartion)
