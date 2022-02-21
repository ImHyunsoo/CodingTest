import random
import time
import collections


def solution(n, t):
    answer = 0
    stack = collections.deque([(0, 0)])
    while stack:
        current_sum, num_idx = stack.popleft()

        if num_idx == len(numbers):
            if current_sum == target:
                answer += 1
        else:
            number = numbers[num_idx]
            stack.append((current_sum+number, num_idx + 1))
            stack.append((current_sum-number, num_idx + 1))
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
