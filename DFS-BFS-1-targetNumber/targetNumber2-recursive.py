import random
import time


def solution(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])


n = random.randint(2, 20)  # 주어지는 숫자의 개수, 2 ~ 20
n = 20
numbers = []
for _ in range(n):
    number = random.randint(1, 50)  # 각 숫자는 1 ~ 50  자연수
    numbers.append(number)
# numbers = [1, 1, 1, 1, 1]

print("n: ", n)
print("numbers: ", numbers)
target = random.randint(1, 1000)  # 타겟 넘버는 1 ~ 1000  자연수
# target = 3
print("target: ", target)

start_time = time.time()

result = solution(numbers, target)
print("result: ", result)

end_time = time.time()
time_duration = end_time - start_time
print("time_duration: ", time_duration)
