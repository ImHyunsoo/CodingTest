import random
import time
import collections

answer = []


def solution(numbers, target):
    global answer
    plus(numbers, 0, 0)
    minus(numbers, 0, 0)
    answer = answer.count(target)
    return answer


def plus(numbers, x, i):
    x += numbers[i]
    if i == len(numbers)-1:
        answer.append(x)
        return answer
    return plus(numbers, x, i+1), minus(numbers, x, i+1)


def minus(numbers, x, i):
    x -= numbers[i]
    if i == len(numbers)-1:
        answer.append(x)
        return answer
    return plus(numbers, x, i+1), minus(numbers, x, i+1)


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

print("--- %s seconds ---" % (time.time() - start_time))
