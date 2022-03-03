import functools


def comparator(a, b):
    return (a+b < b+a) - (b+a < a+b)


def solution(numbers):
    answer = ''
    s_num = list(map(str, numbers))
    print(s_num)
    s_num = sorted(s_num, key=functools.cmp_to_key(comparator))
    print(s_num)

    answer = str(int(''.join(s_num)))
    return answer


# numbers = [3, 30, 34, 5, 9]
numbers = [6, 10, 2]
# numbers = [0, 0]
# return = "9534339"
# return = "6210"
result = solution(numbers)
print(result)
