# 구명보트
import random
import time

n = random.randint(1, 50000)                 # 무인도에 갇힌 사람 1 ~ 50,000 명
# n = 50000
people = []

max_weight = 40                     
for _ in range(n):
    weight = random.randint(40, 240)         # 각 사람의 몸무게 40 ~ 240 kg
    if max_weight < weight:
        max_weight = weight                  # 각 사람들 몸무게 중 최댓값
    people.append(weight)                    # 사람들의 몸무게 리스트 
        
limit = random.randint(max_weight, 240)      # 사람들의 몸무게 중 최댓값보다 큰 구명보트 무게 제한

# print("people: ", people)
# print("n: ", n)
# print("max_weight: ", max_weight)
# print("limit: ", limit)

# 2인 최대, limit 무게
# 일단 내림차순 정렬  
# if max + min > limit    cnt_boat++ (한 명 태움), max인 사람 people 에서 제외 
# else cnt_boat++ (두 명 태움), min, max인 사람 people에서 제외
# 반복 people empty일 때까지
# return cnt_boat 

start_time = time.time()     

people.sort(reverse=True)                    #  people 몸무게, 내림차순 정렬


cnt_boat = 0
idx = 0
while len(people) >= 2 and idx < len(people):
    if people[idx] + people[-1] > limit:        # 몸무게 최댓값과 최솟값의 합이 구명보트 무게 제한 보다 크면 몸무게 최댓값인 사람을 보트 태움
        cnt_boat += 1
        idx += 1
    else:                                     # 몸무게 최댓값과 최솟값의 합이 구명보트 무게 제한 보다 작으면 그 두 사람을 보트에 태움
        cnt_boat += 1
        people.pop(-1)
        idx += 1
        
if len(people) == 1:                          # 사람이 한명 남았다면 그 사람을 보트에 태움
    cnt_boat += 1
    
end_time = time.time()
time_duartion = end_time - start_time
print("time_duartion: ", time_duartion)
    