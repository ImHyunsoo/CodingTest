#  # -*- coding: utf-8 -*-
#  # ū �� �����
# import random
# import time


# num_cnt = random.randint(1, 1000000)  # 1 ~ 1000000 ������ ������ �����ϰ� �����Ǿ� �ڸ����� ��Ÿ��
# # num_cnt = 999999   # �׽�Ʈ
# k = 1 if num_cnt <= 1 else random.randint(1, num_cnt-1)  
# number = ""
# for i in range(num_cnt):
#     number += str(random.randint(0, 9))   # 0 ~ 9 ���� �����ϰ� ���� ���� ���ڿ� ���·� �� �ٿ���

# # print("k: ", k)   
# start_time = time.time()     

# answer = ''
# # number = "4177252841"   # �׽�Ʈ
# # 1924  2  94

# # stack �� �̿��� ū �� ã��
# stack = [number[0]]
# for num in number[1:]:     
#     while len(stack) > 0 and stack[-1] < num and k > 0:
#         k -= 1
#         stack.pop()         # �ڿ� ���� ���ڰ� ũ�� ���ÿ��� �ϳ� ��
#     stack.append(num)       # �ڿ� ���� ���ڰ� ������ ���ÿ� �ϳ� �߰���
# if k != 0:
#     stack = stack[:-k]
# answer = ''.join(stack)


# end_time = time.time()
# time_duartion = end_time - start_time
# print("time_duartion: ", time_duartion)


# # print(''.join(stack))