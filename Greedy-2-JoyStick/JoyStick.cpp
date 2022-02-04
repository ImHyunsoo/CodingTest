// 조이스틱
#include <iostream>
#include <random>
#include <bits/stdc++.h>

using namespace std;

int udCnt = 0 ;

int solution(string name) {
    int answer = 0;
   
    cout << "name: " << name << "  " << name.size() << endl; 

    // 상하 처리  65 ~ 90, 알파벳 바꾸기 카운트
    for (int i = 0; i < name.size(); i++) {
        int num1 = int(name[i]) - int('A');
        int num2 = abs(int(name[i]) - int('Z')-1);
        udCnt += min(num1, num2);
        // cout << name[i] << "  " << int(name[i]) << endl;
        // cout << udCnt << endl; 
    }
    cout << endl;

  
    // 커서 이동 처리
    // A인 곳에서  min(스트레이트, 리턴)
    int move = name.size() - 1;
    int left, right;
    int distance;
    int next_idx;
    
    for (int i = 0; i < name.size(); i++) {
        next_idx = i + 1;
        int tmp1 = 0;
        int tmp2 = 0; 
        if (name[i] == 'A') {           // 'A' 아니라면 straight,     'A' 라면  min(return, straight) 
            while (i + tmp2 >= 0 && name[i + tmp2] == 'A') {          
                tmp2--;
            }
            while (next_idx + tmp1 < name.size() && name[next_idx + tmp1] == 'A') { 
                tmp1++; 
            }
            left = i + tmp2;         
            if(left < 0) left = 0;
            right = name.size() - (next_idx + tmp1);
            cout << "i: " << i << "  left: " << left << "   " << "right: " << right;
            distance = min(left, right);     // 왔다갔다 중복된 이동 거리
            move = min(move, (left + right + distance));   // min(straight, return) 
            cout <<  "  distance: " << distance << "   move: " << move << endl;
        } 
    }
    cout << "udCnt: " << udCnt << "   move: " << move;
    answer = udCnt + move;
    cout << "   answer: " << answer << endl;

    return answer;
}

int main() {
    random_device rd;

    // random_device 를 통해 난수 생성 엔진을 초기화 한다.
    mt19937 gen(rd());
    // mt19937 gen(123);

    // 0 부터 99 까지 균등하게 나타나는 난수열을 생성하기 위해 균등 분포 정의.
    // uniform_int_distribution<int> dis(0, 99);
    uniform_int_distribution<int> dis(65, 90);       // 알파벳 A~Z 아스키코드 중에서 랜덤
    uniform_int_distribution<int> strlen(1, 20);   // 문자열 갯수 1 ~ 20 중에서 랜덤 
    
    // cout << "A: " <<  int('A')  << endl;
    // cout << "Z: " <<  int('Z')  << endl;

    int n = strlen(gen);       // 문자열 갯수 받기
    // cout << "n: " << n << "  "<< char(n) <<'\n';

    // 문자열 생성
    string str = "";
    for (int i = 0; i < n; i++) {
        str += char(dis(gen));
    }


    auto start = std::chrono::steady_clock::now();

    int result;
    result = solution(str);

    auto end = std::chrono::steady_clock::now();
    std::chrono::duration<double> elapsed_seconds = end-start;
    std::cout << "elapsed time: " << elapsed_seconds.count() << "s\n";   // solution 함수  실행 시간

    return 0;
}