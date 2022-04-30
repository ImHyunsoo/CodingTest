def convert_ms(lines):
    end_points_list = []

    for line in lines:
        line = line.split()

        # 응답완료시간 구하기 (ms)
        hour, minute, second = line[1].split(':')
        end_ms = ((int(hour) * 3600 + int(minute) * 60)
                  * 1000 + int(float(second) * 1000))

        # 응답시작시간 구하기 (ms)  (응답시작시간) = (응답완료시간) - (처리시간)
        second = line[2].rstrip('s')
        process_time = int(float(line[2].rstrip('s')) * 1000)

        start_ms = end_ms - process_time + 1  # 처리시간은 시작시간과 끝시간을 포함

        end_points_list.append([start_ms, 's'])  # 라인의 시작점 [응답시작시간, 's']
        end_points_list.append([end_ms, 'e'])  # 라인의 끝점 [응답완료시간, 'e']

    return end_points_list


def solution(lines):
    # 투 포인터
    # lines의 양끝점들을 오름차순으로 정렬 - 이를 기반으로 start를 움직일거임
    # line의 양끝점[시간, 'e or s']을 리스트에 추가

    end_points_list = convert_ms(lines)
    end_points_list.sort(key=lambda x: x[0])

    n = len(end_points_list)  # 라인의 양끝점 데이터의 개수
    ms = 1000  # 1초

    cnt = 0  # 초당 처리량
    max_cnt = 0  # 초당 최대 처리량
    end = 0

    # start를 증가시키며 반복
    for start in range(n):
        # end를 가능한 만큼 이동시키며 카운트
        while end < n and end_points_list[end][0] - end_points_list[start][0] < ms:
            if end_points_list[end][1] == 's':   # 지금 end가 가리키는 곳이 시작점이면 cnt 1 증가
                cnt += 1
            end += 1

        max_cnt = max(cnt, max_cnt)     # 초당 최대 트래픽 저장

        # start가 가리키는 곳이 끝점이었다면 cnt 1 감소
        if end_points_list[start][1] == 'e':
            cnt -= 1

    return max_cnt
