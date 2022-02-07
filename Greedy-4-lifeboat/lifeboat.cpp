#include <random>
#include <string>
#include <vector>
#include <deque>
#include <bits/stdc++.h>

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    
    // 덱 사용
    // 정렬
    // max + min > limit 이면, max 만 태움
    // 아니면, max, min 둘 다 태움

    sort(people.begin(), people.end());                             // 몸무게 오름차순 정렬

    deque<int> d_people (people.begin(), people.end());             // vertor<int>  ->  deque<int> 로 복사

    // 2명 이상이라면 
    // 몸무게 최댓값과 최솟값의 합이 limit 보다 크면, 최댓값인 사람만 태움
    // 몸무게 최댓값과 최솟값의 합이 limit 보다 작으면, 둘 다 태움 
    int cnt = 0;
    while(d_people.size() > 1) {                                
        if (d_people.back() + d_people.front() > limit) {
            d_people.pop_back();
            cnt++;
        }
        else {
            d_people.pop_back();
            d_people.pop_front();
            cnt++;
        }
    }

    // 마지막 한사람 남았다면 그 사람 태움
    if (d_people.size() == 1)
        cnt++;

    answer = cnt;
    return answer;
}

int main() {
    random_device rd;

    // random_device 를 통해 난수 생성 엔진을 초기화 한다.
    mt19937 gen(rd());
    // mt19937 gen(123);

    // 0 부터 99 까지 균등하게 나타나는 난수열을 생성하기 위해 균등 분포 정의.
    // uniform_int_distribution<int> dis(0, 99);
    uniform_int_distribution<int> num_people(1, 50000);       //  무인도에 갇힌 사람은 1명 이상 50,000명 이하
    int n = num_people(gen); 
    // n = 50000;

    uniform_int_distribution<int> weight_person(40, 240);           //  각 사람의 몸무게는 40kg 이상 240kg 이하
    
    // people 몸무게 백터리스트 만들기, 몸무게 최댓값 구하기
    int max_weight = 40;
    vector<int> people;
    for (int i = 0; i < n; i++) {
        int weight = weight_person(gen);
        if (max_weight < weight) max_weight = weight;
        people.push_back(weight);
    }

    // 구명보트의 무게 제한 limit 구하기 (단, 구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없음)
    uniform_int_distribution<int> weight_boat(max_weight, 240);          
    int limit = weight_boat(gen);

    auto start = std::chrono::steady_clock::now();

    int result;
    result = solution(people, limit);

    auto end = std::chrono::steady_clock::now();
    std::chrono::duration<double> elapsed_seconds = end-start;
    std::cout << "elapsed time: " << elapsed_seconds.count() << "s\n";

    return 0;
}