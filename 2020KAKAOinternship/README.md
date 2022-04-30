# 경주로 건설 문제 Lv3
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/67259

## 문제해결 아이디어

###  BFS + DP 
* 상하좌우를 살펴 이동하며 더 적은 비용값으로 업데이트해나가는 방식이다. 이 문제에서 주의할 점은 들어오고 나가는 방향에 따라 코너 추가 비용이 더 들 수 있다는 점이다. 
### 알고리즘
 1. 큐에서 노드를 꺼내 상하좌우를 살피며 맵 영역을 벗어나거나 벽이 아닌 경우, 이전 이동방향과 현재이동 방향이 수직인 경우와 수평인 경우로 나누어 비용계산을 계산한다.
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
https://unho94.tistory.com/m/130

https://ckd2806.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B2%BD%EC%A3%BC%EB%A1%9C-%EA%B1%B4%EC%84%A4

https://ojt90902.tistory.com/537

https://programmers.co.kr/questions/21325

https://programmers.co.kr/questions/17381

https://programmers.co.kr/questions/11840