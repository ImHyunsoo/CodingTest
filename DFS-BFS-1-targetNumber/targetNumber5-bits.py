import random
import time


def solution(n, t):
    answer = 0
    for i in range(2**len(n)):
        tmp = []
        # bitstr = str(bin(i))[2:].zfill(len(n))
        # # print(bitstr)
        # # print(bitstr)
        # for j in range(len(n)):
        #     if bitstr[j] == '1':
        #         tmp.append(n[j])
        #     else:
        #         tmp.append(-n[j])
        # if sum(tmp) == t:
        #     answer += 1

        for j in range(len(n)):
            if i & (2**j) == 0:
                tmp.append(n[j])
            else:
                tmp.append(-1*n[j])
        if sum(tmp) == t:
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
