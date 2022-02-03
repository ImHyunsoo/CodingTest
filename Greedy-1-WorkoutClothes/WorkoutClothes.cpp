// 체육복
#include <iostream>
#include <random>
#include <bits/stdc++.h>

using namespace std;

int cnt;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    vector<int> _lost = lost;
    vector<int> _reserve = reserve;

    cout << "n: " << n << endl;
    cout << "lost: ";
    for (int i = 0; i < lost.size(); i++) {
        cout << lost[i] << ' ';        
    }
    cout << endl;

    cout << "reserve: ";
    for (int i = 0; i < reserve.size(); i++) {
        cout << reserve[i] << ' '; 
    }
    cout << endl;

  
    
    // 중복 처리
    for(int i = 0; i < lost.size(); i++) {
        _reserve.erase(remove(_reserve.begin(), _reserve.end(), lost[i]), _reserve.end());
    }
    for(int i = 0; i < reserve.size(); i++) {
        _lost.erase(remove(_lost.begin(), _lost.end(), reserve[i]), _lost.end());
    }
    cout << endl << "overlapping treatment" << endl;
    cout << "lost: ";
    for(int i = 0; i< _lost.size(); i++) {
        cout << _lost[i] << ' '; 
    }
    cout << endl << "reserve: ";
    for(int i = 0; i< _reserve.size(); i++) {
        cout << _reserve[i] << ' '; 
    }
    cout << endl << endl;


    //     if (*find(data_types.begin(), data_types.end(), element_to_check1) == element_to_check1) 

    // 여벌있는 사람은 앞에서 부터 순차적으로 앞에 줄 사람 있으면 주고 없으면 뒷 사람 줄 사람 주자
    for(int i = 0; i < _reserve.size(); i++) {
        int f = _reserve[i] - 1;
        int b = _reserve[i] + 1;
        if(*find(_lost.begin(), _lost.end(), f) == f)
            _lost.erase(remove(_lost.begin(), _lost.end(), f), _lost.end());
        else if (*find(_lost.begin(), _lost.end(), b) == b) 
            _lost.erase(remove(_lost.begin(), _lost.end(), b), _lost.end());
    }

    cout << "_lost: ";
    for(int i = 0; i< _lost.size(); i++) {
        cout << _lost[i] << ' '; 
    }
    cout << endl;

    answer = n - _lost.size();
  
    return answer;
}

vector<int> GenRandom(int n) {
    vector<int> array; 

    // 시드값을 얻기 위한 random_device 생성.
    random_device rd;

    // random_device 를 통해 난수 생성 엔진을 초기화 한다.
    mt19937 gen(rd());
    // mt19937 gen(123);

    // 0 부터 99 까지 균등하게 나타나는 난수열을 생성하기 위해 균등 분포 정의.
    // uniform_int_distribution<int> dis(0, 99);
    uniform_int_distribution<int> dis(1, n);
    
    // 중복되지 않게 랜덤한 학생 뽑기
    int visited_test[n];
    memset(visited_test, 0, n*4);
    // for (int i = 0; i < n; i++) {
    //      cout << visited_test[i];
    // }
    // cout << endl;
    
    int k = dis(gen);

    for(int i = 0; i < k; i++) {
        while(true) {
            int num = dis(gen);
            if (visited_test[num-1] == 0){
                visited_test[num-1] = 1;
                array.push_back(num);
                break;
            }
        }
    }

    // for (int i = 0; i < n; i++) {
    //     cout << visited_test[i];
    // }
    // cout << endl;


    return array;
}




int main() {

    for(int x = 0; x < 20; x++){           // 20번 테스트
        int n;
        vector<int> lost;
        vector<int> reserve;
        

        random_device rd;

        // random_device 를 통해 난수 생성 엔진을 초기화 한다.
        mt19937 gen(rd());
        // mt19937 gen(123);

        // 0 부터 99 까지 균등하게 나타나는 난수열을 생성하기 위해 균등 분포 정의.
        // uniform_int_distribution<int> dis(0, 99);
        uniform_int_distribution<int> dis(2, 30);
        
        n = dis(gen);
        // cout << "n: " << n <<'\n';
    ///////////////////////////////////////////////////////////////////////

        // 난수 기본 예제
        // for (int i = 0; i < 5; i++) {
        //     cout << "난수 : " << dis(gen) << endl;
        
        // }
        
        //////////////////////////////////////////////////////////

        /// 중복되고 있음
        // int k = dis(gen);
        // for (int i = 0; i < k; i++) {
        //     lost.push_back(dis(gen));
        //     // cout << "lost[" << i << "]: " << lost[i] << '\n';
        // }

        // k = dis(gen);
        // for (int i = 0; i < k; i++) {
        //     reserve.push_back(dis(gen));
        //     // cout << "reserve[" << i << "]: " << reserve[i] << '\n';
        // }

        //////////////////////////////////////////////////////////////////

        
        lost = GenRandom(n);         // 중복 없이 체육복 잃어버린 학생
        reserve = GenRandom(n);       // 중복 없이 체육복 여분있는 학생

        auto start = std::chrono::steady_clock::now();
        
        sort(lost.begin(), lost.end());          // 번호 순대로 정렬
        sort(reserve.begin(), reserve.end());
        
        cout << endl;
        int result = solution(n, lost, reserve);
        cout << "result: " << result << '\n';
        
        auto end = std::chrono::steady_clock::now();
        std::chrono::duration<double> elapsed_seconds = end-start;
        std::cout << "elapsed time: " << elapsed_seconds.count() << "s\n";   // solution 함수  실행 시간
        cout << endl << endl << endl;
    }

    return 0;
}
