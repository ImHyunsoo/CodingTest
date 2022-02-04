// 큰 수 만들기
#include <iostream>
#include <random>
#include <bits/stdc++.h>

using namespace std;


string solution(string name, int k) {
    string answer = "";
   
    // stack 이용
    // 앞에서 부터 담고 뒤에 오는 숫자가 더 크면 앞에꺼랑 비교해서 크면 앞에꺼 버리기 
    // 비교해서 작으면  스택에 추가 
    //  스택이 비어있으면 숫자 추가
    answer.push_back(name[0]);
    for (int i = 1; i < name.size(); i++) {
        while (answer.size() > 0 && k > 0 && answer.back() < name[i]) {
            answer.pop_back();
            k--;      
        } 
        answer.push_back(name[i]);
    }
    answer = answer.substr(0, answer.size()-k);    // 전체 문자열 길이에서 k개 만큼 뺀 문자열
    
    return answer;
}


int main() {
    random_device rd;

    // random_device 를 통해 난수 생성 엔진을 초기화 한다.
    mt19937 gen(rd());
    // mt19937 gen(123);

    // 0 부터 99 까지 균등하게 나타나는 난수열을 생성하기 위해 균등 분포 정의.
    // uniform_int_distribution<int> dis(0, 99);
    uniform_int_distribution<int> dis_num_len(1, 1000000);

    int number_len = dis_num_len(gen);
    // number_len = 999999;

    uniform_int_distribution<int> dis_remove_len(1, number_len-1);   // 문자열 갯수
    int k = dis_remove_len(gen);



    uniform_int_distribution<int> dis_number(0, 9);
    string name = "";
    for (int i = 0; i < number_len; i++) {
        name += dis_number(gen)  + '0';
        // cout << name  << endl;
        // this_thread::sleep_for (std::chrono::seconds(1));
    }

    auto start = std::chrono::steady_clock::now();

    string result;
    result = solution(name, k);

    auto end = std::chrono::steady_clock::now();
    std::chrono::duration<double> elapsed_seconds = end-start;
    std::cout << "elapsed time: " << elapsed_seconds.count() << "s\n";

    return 0;
}
