import random
import time
import itertools  # 모든 조합을 위해!


def solution(numbers, target):
    combination_list = list()
    combination_list.append(list())
    for number in numbers:
        combination_list = combination(combination_list, number)

    answer = 0
    for item in combination_list:
        if sum(item) == target:
            answer += 1

    return answer


def combination(prevCombination, number):
    newCombination = list()
    for item in prevCombination:
        newCombination.append(item + [number])
        newCombination.append(item + [-1 * number])
    return newCombination


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
