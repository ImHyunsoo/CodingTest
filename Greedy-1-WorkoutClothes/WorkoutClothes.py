# 체육복
import random
import copy
import time

n = random.randint(2, 30)
k = random.randint(1, n)
m = random.randint(1, n)
lost = random.sample(range(1, n+1), k)       # 중복없이,  1 ~ n  중에서  랜덤한 수 k개를 뽑음
reserve = random.sample(range(1, n+1), m)
print("학생 랜덤")
print(n)
print(lost, k)
print(reserve, m)
print()

start_time = time.time()     

print("학생 번호 정렬")
lost.sort()      # 체육복 잃어버린 학생 번호 순으로 정렬
reserve.sort()    # 체육복 여유분 있는 학생 번호 순으로 정렬
print(lost, len(lost))
print(reserve, len(reserve))
print()

lost2 = copy.deepcopy(lost)
reserve2 = copy.deepcopy(reserve)


# 체육복 여유분 가져오기도 하고 잃어버리기도 한 학생 제외 
print("중복 제거")
for re_stu in reserve:
    if re_stu in lost2:
        lost2.remove(re_stu)
print(lost2, len(lost2))
for lo_stu in lost:
    if lo_stu in reserve2:
        reserve2.remove(lo_stu)
print(reserve2, len(reserve2))
print()

for re2_stu in reserve2:
    f = re2_stu - 1
    b = re2_stu + 1
    if f in lost2:
        lost2.remove(f)
    elif b in lost2:
        lost2.remove(b)
        
result = n - len(lost2)
print(result)

# time.sleep(1)
end_time = time.time()
time_duartion = end_time - start_time
print("time_duartion: ", time_duartion)