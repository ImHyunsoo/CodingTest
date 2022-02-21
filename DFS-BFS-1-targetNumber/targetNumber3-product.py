import random
import time
from itertools import product


def solution(numbers, target):
    # data = [(1, 2), (3, 4), (5, 6)]
    # print(data)
    # print(*data)
    # print(list(product(data)))
    # print(list(product(*data)))

    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)


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
