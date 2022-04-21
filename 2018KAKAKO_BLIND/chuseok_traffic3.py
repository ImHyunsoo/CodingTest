# https://rain-bow.tistory.com/entry/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-2018-KAKAO-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%B6%94%EC%84%9D-%ED%8A%B8%EB%9E%98%ED%94%BD-1

# 구간 선택방법 - 각 프로세스 별 끝 시간을 기준으로 +1초를 '구간'으로 정의
# 시작아닌 끝 시간을 설정한 이유는, 구해야하는 것은 '최대 처리량;이며 처리량은 '시작시간과 끝시간을 포함'함
# 따라서 끝시간을 포함하는 +1초 내에 해당 프로세스 구간을 구하는 것이 시작 시간을 포함하는 +1초 구간을 설정하는 것보다 계산적으로 좋음
# 그 이전 구간은 생각하지 않아도 되니까요

# 각 구간에 몇 개의 프로세스가 존재하는지를 전체 프로세스에 대해 체크
# N개 로그가 주어졌을 때 기준점은 N개가 되고 N개의 구간에 대해 N개의 프로세스들을 체크해보면 됨. O(N^2)
# 제한 조건 중 최대 T가 3s라는 것을 생각해볼 때, 구간의 최대 길이보다 +3초 이상을 start_time으로 갖는 프로세스는 해당 구간에서 검사할 필요 없음
# 이상적인 경우 O(nlogn)

def parsing_line(line):
    _, S, T = line.split(' ')
    time = S.split(":")
    time = list(map(float, time))
    end_time = convert_time_to_second(time)
    ptime = T.split('s')
    ptime = float(ptime[0])
    start_time = end_time - ptime + 0.001
    start_time = round(start_time, 3)  # 소수점 3자리 반올림
    return start_time, end_time


def convert_time_to_second(time):  # 시간을 초로 변경
    assert len(time) == 3
    return 3600 * time[0] + 60 * time[1] + float(time[2])


def solution(lines):
    length = len(lines)
    max_ = 1
    max_time = 0
    for i in range(length - 1):
        line = lines[i]
        start_time, end_time = parsing_line(line)
        ptime = end_time + 1.0
        count = 1

        for j in range(i + 1, length):
            line = lines[j]
            next_start_time, next_end_time = parsing_line(line)
            if next_end_time >= ptime + 3.0:  # 다음 트래픽의 종료 시간이 3.0s 이상 차이난다면 종료
                break  # 이 break문을 통해 알고리즘 속도 개선 가능
            if next_start_time < ptime:
                count += 1  # 처리량 +1
            max_ = max(max_, count)  # 최대 처리량 구하기
    return max_


lines = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s",
         "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]
# lines = ["2016-09-15 00:00:00.000 3s"]  # 1 // o
# lines = ["2016-09-15 23:59:59.999 0.001s"]  # 1 // o
# lines = ["2016-09-15 01:00:04.001 2.0s",
#          "2016-09-15 01:00:07.000 2s"]  # 1 // o
# lines = ["2016-09-15 01:00:04.002 2.0s",
#          "2016-09-15 01:00:07.000 2s"]  # 2 // o
# lines = ["2016-09-15 00:00:00.000 2.3s",
#  "2016-09-15 23:59:59.999 0.1s"]  # 1 // o
result = solution(lines)
print(result)
