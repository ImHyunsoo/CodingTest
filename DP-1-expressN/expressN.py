def combi(A, B):
    result = set()
    for a in A:
        for b in B:
            result |= {a*b}
            if b != 0:
                result |= {a//b}
            result |= {a+b}
            result |= {a-b}
    return result


def solution(N, number):
    d = [-1] * 10
    d[0] = {0}
    d[1] = {N}
    if number == N:
        return 1

    for i in range(2, 9):
        tmp = set()
        for j in range(1, i):
            tmp |= combi(d[j], d[i-j])
        tmp |= {int(str(N)*i)}
        d[i] = tmp
        if number in d[i]:
            return i
    return -1


N = 5
number = 26
print(solution(N, number))
'''
N	number	return
5	12  	4
2	11	    3
[{0}, {5}, {0, 1.0, 10, 55, 25}, {0, 2, 4.0, 5, 6.0, 5001, 11, 525, -50, 15.0, 275, 20, 30, 105, 555, -4.0, -20, 50, -5, 60, 125, 510, 255}, {0, 1.0, 2, 3, 4, 5, 6, 7, 520, 9.0, 10, 11.0, -250, 525, 270, 15, 16, -495, 530, 12, 20.0, 21, -505, 1275, 280, 25, 10001, 26.0, 24.0, 260, 30.0, 1055, 2550, 515, 35, 550, 1025, 300, 45.0, 560, 305, 50, 51, 52, 54.0, 55, 2555, 56.0, -195, 65.0, 2625, 75.0, 49996, 80, 4950, 605, 50015, 1375, 100, 102, 105, 110, 111, 625, 115, 4980, 120, -4996, 125.0, 130, 4996, 5510, 5255, -120, 5004, 5006, 5525, 150, 155.0, 5275, -100, 25001, 25005, 5555, 5125, 2755, -55, -54.0, 205, 2510, 3025, -45, -9.0, 2775, 55001, -550, -35.0, 2525, -30, -25, 1000, 1255, 250, 1001.0, -20.0, -24.0, 495, -15, -270, 5105, 1010, -10, -2.0, -520, 505, -6, -5, -4, -3, -1.0, 511}, -1, -1, -1, -1, -1]

'''
