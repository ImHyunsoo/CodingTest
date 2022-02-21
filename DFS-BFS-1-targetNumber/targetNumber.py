import random
import time


def dfs(x, tmp_target):
    global result
    tmp_target1 = tmp_target + numbers[x]
    tmp_target2 = tmp_target - numbers[x]
    if x == n-1:
        if tmp_target1 == target:
            result += 1
        if tmp_target2 == target:
            result += 1
        return

    dfs(x+1, tmp_target1)
    dfs(x+1, tmp_target2)


n = random.randint(2, 20)  # 주어지는 숫자의 개수, 2 ~ 20
n = 20
numbers = []
for _ in range(n):
    number = random.randint(1, 50)  # 각 숫자는 1 ~ 50  자연수
    numbers.append(number)
# numbers = [1, 1, 1, 1, 1]

print(n)
print(numbers)
target = random.randint(1, 1000)  # 타겟 넘버는 1 ~ 1000  자연수
# target = 3
print(target)

'''
갯수 20
2^20
1024 
1000000 > 10 ^ 6   // 파이썬 1초, 20 * 10^6 연산
>> 0.05초?

정렬 
같은 수 

dfs 타켓 보다 작으면 +  아니면 -

+  +-   +- +-   +-+- +-+-

-  
'''
result = 0
tmp_target = 0

start_time = time.time()

dfs(0, tmp_target)
print("result: ", result)

end_time = time.time()
time_duration = end_time - start_time
print("time_duration: ", time_duration)
