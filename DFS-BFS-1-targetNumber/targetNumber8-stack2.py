import random
import time


def solution(numbers, target):
    answer = 0
    queue = [(0, 0)]
    length = len(numbers)

    while queue:
        n = queue.pop()
        if n[0] < length:
            queue.append((n[0] + 1, n[1] + numbers[n[0] - 1]))
            queue.append((n[0] + 1, n[1] - numbers[n[0] - 1]))
        elif n[1] == target:
            answer += 1

    return answer


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
