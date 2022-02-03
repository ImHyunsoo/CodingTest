// ü����
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

  
    
    // �ߺ� ó��
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

    // �����ִ� ����� �տ��� ���� ���������� �տ� �� ��� ������ �ְ� ������ �� ��� �� ��� ����
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

    // �õ尪�� ��� ���� random_device ����.
    random_device rd;

    // random_device �� ���� ���� ���� ������ �ʱ�ȭ �Ѵ�.
    mt19937 gen(rd());
    // mt19937 gen(123);

    // 0 ���� 99 ���� �յ��ϰ� ��Ÿ���� �������� �����ϱ� ���� �յ� ���� ����.
    // uniform_int_distribution<int> dis(0, 99);
    uniform_int_distribution<int> dis(1, n);
    
    // �ߺ����� �ʰ� ������ �л� �̱�
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

    for(int x = 0; x < 20; x++){           // 20�� �׽�Ʈ
        int n;
        vector<int> lost;
        vector<int> reserve;
        

        random_device rd;

        // random_device �� ���� ���� ���� ������ �ʱ�ȭ �Ѵ�.
        mt19937 gen(rd());
        // mt19937 gen(123);

        // 0 ���� 99 ���� �յ��ϰ� ��Ÿ���� �������� �����ϱ� ���� �յ� ���� ����.
        // uniform_int_distribution<int> dis(0, 99);
        uniform_int_distribution<int> dis(2, 30);
        
        n = dis(gen);
        // cout << "n: " << n <<'\n';
    ///////////////////////////////////////////////////////////////////////

        // ���� �⺻ ����
        // for (int i = 0; i < 5; i++) {
        //     cout << "���� : " << dis(gen) << endl;
        
        // }
        
        //////////////////////////////////////////////////////////

        /// �ߺ��ǰ� ����
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

        
        lost = GenRandom(n);         // �ߺ� ���� ü���� �Ҿ���� �л�
        reserve = GenRandom(n);       // �ߺ� ���� ü���� �����ִ� �л�

        auto start = std::chrono::steady_clock::now();
        
        sort(lost.begin(), lost.end());          // ��ȣ ����� ����
        sort(reserve.begin(), reserve.end());
        
        cout << endl;
        int result = solution(n, lost, reserve);
        cout << "result: " << result << '\n';
        
        auto end = std::chrono::steady_clock::now();
        std::chrono::duration<double> elapsed_seconds = end-start;
        std::cout << "elapsed time: " << elapsed_seconds.count() << "s\n";   // solution �Լ�  ���� �ð�
        cout << endl << endl << endl;
    }

    return 0;
}
