#  # -*- coding: utf-8 -*-
#  # 큰 수 만들기
# import random
# import time


# num_cnt = random.randint(1, 1000000)  # 1 ~ 1000000 사이의 정수가 랜덤하게 생성되어 자리수를 나타냄
# # num_cnt = 999999   # 테스트
# k = 1 if num_cnt <= 1 else random.randint(1, num_cnt-1)  
# number = ""
# for i in range(num_cnt):
#     number += str(random.randint(0, 9))   # 0 ~ 9 에서 랜덤하게 뽑힌 수를 문자열 형태로 덧 붙여줌

# # print("k: ", k)   
# start_time = time.time()     

# answer = ''
# # number = "4177252841"   # 테스트
# # 1924  2  94

# # stack 을 이용한 큰 수 찾기
# stack = [number[0]]
# for num in number[1:]:     
#     while len(stack) > 0 and stack[-1] < num and k > 0:
#         k -= 1
#         stack.pop()         # 뒤에 오는 숫자가 크면 스택에서 하나 뺌
#     stack.append(num)       # 뒤에 오는 숫자가 작으면 스택에 하나 추가함
# if k != 0:
#     stack = stack[:-k]
# answer = ''.join(stack)


# end_time = time.time()
# time_duartion = end_time - start_time
# print("time_duartion: ", time_duartion)


# # print(''.join(stack))