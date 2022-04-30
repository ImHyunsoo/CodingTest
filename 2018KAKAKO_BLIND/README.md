# 추석 트래픽 문제 Lv3
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/67259

## 문제분석 
* 첫 로그 시각부터 마지막 로그 시각까지 1ms씩 증가시키면서 1000ms 단위의 슬라이딩 윈도우로 풀면 24 * 3600 * 1000 * n * 1000ms 만큼의 연산이 필요하기 때문에 이렇게는 풀 수가 없다.
* 각 로그의 시작 시각부터 마지막 시각까지 1ms 씩 움직이면 time(ms) * n^2 이 되며, time(ms)의 값은 대부분 천 단위 이상이기 때문에 타임아웃이 발생하여 풀 수가 없다.
* 요청량이 변하는 순간은 각 로그의 시작과 끝뿐이다. 따라서, 각 로그 별 2번의 비교 연산만 수행하면 되며 2 * n^2, 빅오로 정리하면 O(n^2)에 풀 수가 있다.
* 제한 조건 중 최대 T가 3s라는 것을 생각해볼 때, 구간의 최대 길이보다 +3초 이상을 start_time으로 갖는 프로세스는 해당 구간에서 검사할 필요가 없다. 이 경우 이상적인 경우 O(nlogn)에 풀 수 있다.
* 투 포인터가 각 로그의 시작과 끝을 이동하며 비교 연산을 수행하면 O(n)에 풀 수 있다.

## 문제 핵심 아이디어
### 투포인터를 활용한 알고리즘
 1. 라인 정보를 파싱해서 각 로그의 시작과 끝 시간을 ms단위로 변환하고 시작인지 끝인지 정보와 함께 리스트에 오름차순 정렬한다. 
 2. 다음노드에 기록되어있는 비용보다 같거나 더 적은 비용이 든다면 노드의 방향과 비용을 업데이트하고 bfs 큐에 추가합니다.
 3. 과정 1~2를 반복하며 더 이상 방문할 노드가 없다면 목표노드의 비용을 반환합니다. 

* [첫 번째 풀이](constructionRaceway1.py)

### 문제 발생 

#### 반례 테스터케이스
* 입력값: [[0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1], [
    1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0]]
* 기댓값: 4500
* 실행결과: 4900

* 위 테스터케이스의 일부를 발췌한 표가 아래에 있다. 왼쪽에서 오는 경로와 오른쪽에서 오는 경로가 강조된 부분에서 만나 아래로 업데이트하는 상황이다. 위 알고리즘은 강조된 노드의 비용을 최소값 2700으로 업데이트하였다. 

...|...|...|...|...|...
:---:|:---:|:---:|:---:|:---:|:---:|
...|1400|1|2200|2100|...|
...|2000|2600|**`2700`**|1|...|
...|1|1|3300|3900|...|

* 하지만 최종 목표노드의 비용값이 최소가 되어야하므로 강조된 부분에서 2700은 2800이 되어야하고 그 밑은 2900으로 업데이트 되어야 한다.

...|...|...|...|...|...
:---:|:---:|:---:|:---:|:---:|:---:|
...|1400|1|2200|2100|...|
...|2000|2600|**`2800`**|1|...|
...|1|1|2900|3500|...|

## 개선 아이디어
* 강조된 노드의 아래 노드 2900 은 어떻게 업데이트되어야 할까? 강조된 노드가 자신에게 들어온 방향을 가지고 있고 각 방향별로 최소 비용을 가지고 있다면 이를 바탕으로 아래 노드의 최소비용값을 계산할 수 있다. 위 테스트 케이스를 예로 들자면 강조된 노드는 왼쪽에서 들어온 비용 2700과 위쪽에서 들어돈 비용 2800을 가지고 있다. 아래노드는 이 정보를 기반으로 각 비용 3300과 2900을 계산할 수 있고 이중 최솟값을 위쪽에서 들어온 비용으로 업데이트할 수 있다. 
    
### 개선 알고리즘
 1. 큐에서 노드를 꺼내 상하좌우를 살피며 맵 영역을 벗어나거나 벽이 아닌 경우, 다음 노드로 들어가는 방향을 고려하여 최소 비용값을 구한다.
 2. 다음노드가 가지고 있는 해당 방향과 그 비용값을 비교하여 더 적은 비용이면 해당방향의 비용값을 업데이트하고 bfs 큐에 추가한다.
 3. 과정 1~2를 반복하며 더 이상 방문할 노드가 없다면 목표노드의 비용을 반환합니다. 

* [개선한 두 번째 풀이](constructionRaceway2.py)

## 참고
https://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/



https://ckd2806.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B2%BD%EC%A3%BC%EB%A1%9C-%EA%B1%B4%EC%84%A4

https://ojt90902.tistory.com/537

https://programmers.co.kr/questions/21325

https://programmers.co.kr/questions/17381

https://programmers.co.kr/questions/11840