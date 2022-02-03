# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# # # 체육복
# import random



# n = random.randint(2, 30)
# k = random.randint(1, n)
# m = random.randint(1, n)
# lost = random.sample(range(1, n+1), k)
# reserve = random.sample(range(1, n+1), m)
# print(n)
# print(lost, k)
# print(reserve, m)
# print()

# ########################################################################
# # lost_set = set(lost) - set(lost).intersection(set(reserve))
# # reserve_set = set(reserve) - set(lost).intersection(set(reserve))
# # print(lost_set)
# # print(reserve_set)
# # for i in list(reserve_set):
# #     if int(i)-1 in lost_set:
# #         lost_set -= {int(i)-1}
# #     elif int(i)+1 in lost_set:
# #         lost_set -= {int(i)+1}
# # print(n - len(lost_set))

# ################################################################33


# survive = 0
# cloth_cnt = [1] * n
# print(cloth_cnt)

# for i in lost:
#     cloth_cnt[i-1] -= 1

# print(cloth_cnt)

# for j in reserve:
#     cloth_cnt[j-1] += 1
    
# print(cloth_cnt)

# for i in lost:
#     if i in reserve:
#         survive += 1

# # 나에게 빌려줄 수 있는 사람이 오직 한사람 뿐인 사람

# # 첫 번째랑 마지막 번째 학생 먼저 처리 
# if cloth_cnt[0] == 0 and cloth_cnt[1] == 2:
#     cloth_cnt[0] = 1
#     cloth_cnt[1] = 1
#     survive += 1
    
# if cloth_cnt[n-1] == 0 and cloth_cnt[n-2] == 2:
#     cloth_cnt[n-1] = 1
#     cloth_cnt[n-2] = 1
#     survive += 1
    
# print("첨과 끝 먼저 처리")    
# print(cloth_cnt)
    
# temp = survive    
# while True:    
#     # 여유 없는 사람 처리
    
#     for i in range(1, n-1):
#         if cloth_cnt[i] == 0:
#             if cloth_cnt[i-1] == 2 and cloth_cnt[i+1] == 2:
#                 continue
#             elif cloth_cnt[i+1] == 2:
#                 cloth_cnt[i] = 1
#                 cloth_cnt[i+1] = 1
#                 survive += 1
#             elif cloth_cnt[i-1] == 2:
#                 cloth_cnt[i] = 1
#                 cloth_cnt[i-1] = 1
#                 survive += 1
#     if temp == survive:
#         break
#     else: 
#         temp = survive
            
# print(cloth_cnt)         

# # 여유 있는 사람 처리
# for i in range(1, n-1):
#     if cloth_cnt[i] == 0:
#         if cloth_cnt[i-1] == 2 and cloth_cnt[i+1] == 2: 
#             survive += 1
#             # cloth_cnt[i] = 1
#             # cloth_cnt[i+1] = 1
            

        
# answer = n - len(lost) + survive 
# print(answer, " = ", n, " - ", k, " + ", survive )

