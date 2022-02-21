import random
import time
import itertools  # 모든 조합을 위해!


def solution(numbers, target):
    answer = 0
    asum = 0
    alist = []
    goal = sum(numbers)-target
    for i in range(len(numbers)):
        alist.append(i)
    for j in range(len(numbers)):
        mypermutation = itertools.combinations(alist, j+1)
        print(list(mypermutation))
        for s in mypermutation:  # 각 조합에서의 모든 경우에서
            for k in s:
                asum = asum + numbers[k]*2
                '''
                여기서 mypermutation은 [ - 연산을 적용할 number의 조합 ] 입니다. 
                각 조합이 target을 만드는지 알기 위해 [ 조합 내 원소들이 + 에서 - 연산으로 바뀌었을 때
                결과값의 변화 ]를 계산해 goal과 비교합니다. 그래서 [ numbers[k]를 1번 포함해 + 연산을 취소하고, 
                1번 더 포함해 - 연산으로 바꿔 ] 변화량을 구합니다. 이걸 numbers[k]*2로 나타낸 것 같습니다.
                '''

            if asum == goal:
                answer = answer + 1
            asum = 0
    return answer


n = random.randint(2, 20)  # 주어지는 숫자의 개수, 2 ~ 20
n = 4
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
