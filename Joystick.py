# # -*- coding: utf-8 -*-
# # 가독성 좋게 다시 코딩해볼 것
# # # a b c d e f g h i j k l m n o p q r s t u v w x y z
# # 조이스틱

# def solution(name):
#   cnt = 0
#   idx = 0   
#   answer = 0

#   value_name = ""
#   list_value_name = []
#   list_name = []
#   print()
#   print()
#   # 문자열 초기화  AAAA...
#   for i in range(len(name)):
#       value_name += 'A'
#       list_value_name.append('A')
#       list_name.append(name[i])
#   print("len(name): ", len(name))


#   #####################################################
#   # for 문  역순 
#   #  print("len(name): ", len(name))
#   #  for i in range((len(name)-1), -1, -1):
#   #      print(i)
#   # for 문  
#   #  print("len(name): ", len(name))
#   #  for i in range(1, len(name)):
#   #      print(i)
#   ##############################################################

#   while True:
#       # 알바벳 교정 체크    # 상하 move count
#       diff1 = ord(name[idx]) - ord(list_value_name[idx])
#       diff2 = ord(name[idx]) - (ord(list_value_name[idx]) + 26)
#       if diff1 == 0 or diff2 == 0:
#           pass
#       else: 
#           if abs(diff1) <= abs(diff2):
#               cnt += abs(diff1)
#               list_value_name[idx] = name[idx]
#           else: 
#               cnt += abs(diff2)
#               list_value_name[idx] = name[idx]

#       print(name)
#       print(list_name)
#       print(list_value_name)
#       print("cnt: ", cnt)

    
#       # 문자열 완성 체크
#       check = True
#       for i in range(len(name)):
#           if list_value_name[i] != name[i]:
#               check = False
#               break
#       if check == True:
#           break
          
#       # 커서 이동
#       l_min = 20
#       r_min = 20
#       for k in range(1, len(name)):
#           r_idx = idx + k
#           l_idx = idx - k

#           if r_idx >= len(name):
#               r_idx -= len(name) 

#           if l_idx <= -1:
#               l_idx += len(name)  



#           r_dist_left_end = 0
#           for i in range(1, len(name)-1):
#               new_idx = r_idx + i
#               if new_idx >= len(name):
#                   new_idx -= len(name)
#               if list_value_name[new_idx] == name[new_idx]:
#                   r_dist_left_end += 1
#               else: 
#                   break
#           r_dist_left = len(name) -1 - r_dist_left_end
              
#           r_dist_right_end = 0
#           for i in range(1, len(name)-1):
#               new_idx = r_idx - i
#               if new_idx <= -1:
#                   new_idx += len(name) 
#               if list_value_name[new_idx] == name[new_idx]:
#                   r_dist_right_end += 1
#               else:
#                   break
#           r_dist_right = len(name) -1 - r_dist_right_end 
          
#           if r_dist_left >= r_dist_right:
#               r_dist_min = r_dist_right + k
#           else:
#               r_dist_min = r_dist_left + k


#           l_dist_left_end = 0
#           for i in range(1, len(name) -1):
#               new_idx = l_idx + i
#               if new_idx >= len(name):
#                   new_idx -= len(name)
#               if list_value_name[new_idx] == name[new_idx]:
#                   l_dist_left_end += 1
#               else:
#                   break        
#           l_dist_left = len(name) -1 - l_dist_left_end

#           l_dist_right_end = 0
#           for i in range(1, len(name) -1):
#               new_idx = l_idx - i
#               if new_idx <= -1:
#                   new_idx += len(name)
#               if list_value_name[new_idx] == name[new_idx]:
#                   l_dist_right_end += 1
#               else:
#                   break
#           l_dist_right = len(name) -1 - l_dist_right_end

#           if l_dist_left >= l_dist_right:
#               l_dist_min = l_dist_right + k
#           else: 
#               l_dist_min = l_dist_left + k

#               ###################################################
          
#           if l_min >= l_dist_min:
#               l_min = l_dist_min
#           if r_min >= r_dist_min:
#               r_min = r_dist_min

#           print("r_dist_left: ", r_dist_left, "    r_dist_right: ", r_dist_right)

          
#           print("l_dist_left: ", l_dist_left, "    l_dist_right: ", l_dist_right)
#           print()
#           print("r_dist_min: ", r_dist_min,  "    l_dist_min: ", l_dist_min)
#           print()


#       print()
#       print("r_min: ",r_min, "         l_min: ",l_min)

#       if r_min >= l_min:
#           cnt += 1
#           idx -= 1
#       else:
#           cnt += 1
#           idx += 1

#       if idx == len(name):
#           idx = 0
#       if idx == -1:
#           idx = len(name)-1

#       print("idx: ", idx)

#   answer = cnt

#   return answer


     


# import random
# import time

# name = ""
# n = random.randint(1, 20)        # 글자 수는 1~20 중에서 랜덤하게 뽑힘
# for _ in range(n):
#     name += chr(random.randint(65, 90))   # 대문자 알파벳 문자열에 추가하기
# print(name)


# result = solution(name)