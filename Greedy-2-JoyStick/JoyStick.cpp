// ���̽�ƽ
#include <iostream>
#include <random>
#include <bits/stdc++.h>

using namespace std;

int udCnt = 0 ;

int solution(string name) {
    int answer = 0;
   
    cout << "name: " << name << "  " << name.size() << endl; 

    // ���� ó��  65 ~ 90, ���ĺ� �ٲٱ� ī��Ʈ
    for (int i = 0; i < name.size(); i++) {
        int num1 = int(name[i]) - int('A');
        int num2 = abs(int(name[i]) - int('Z')-1);
        udCnt += min(num1, num2);
        // cout << name[i] << "  " << int(name[i]) << endl;
        // cout << udCnt << endl; 
    }
    cout << endl;

  
    // Ŀ�� �̵� ó��
    // A�� ������  min(��Ʈ����Ʈ, ����)
    int move = name.size() - 1;
    int left, right;
    int distance;
    int next_idx;
    
    for (int i = 0; i < name.size(); i++) {
        next_idx = i + 1;
        int tmp1 = 0;
        int tmp2 = 0; 
        if (name[i] == 'A') {           // 'A' �ƴ϶�� straight,     'A' ���  min(return, straight) 
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
            distance = min(left, right);     // �Դٰ��� �ߺ��� �̵� �Ÿ�
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

    // random_device �� ���� ���� ���� ������ �ʱ�ȭ �Ѵ�.
    mt19937 gen(rd());
    // mt19937 gen(123);

    // 0 ���� 99 ���� �յ��ϰ� ��Ÿ���� �������� �����ϱ� ���� �յ� ���� ����.
    // uniform_int_distribution<int> dis(0, 99);
    uniform_int_distribution<int> dis(65, 90);       // ���ĺ� A~Z �ƽ�Ű�ڵ� �߿��� ����
    uniform_int_distribution<int> strlen(1, 20);   // ���ڿ� ���� 1 ~ 20 �߿��� ���� 
    
    // cout << "A: " <<  int('A')  << endl;
    // cout << "Z: " <<  int('Z')  << endl;

    int n = strlen(gen);       // ���ڿ� ���� �ޱ�
    // cout << "n: " << n << "  "<< char(n) <<'\n';

    // ���ڿ� ����
    string str = "";
    for (int i = 0; i < n; i++) {
        str += char(dis(gen));
    }


    auto start = std::chrono::steady_clock::now();

    int result;
    result = solution(str);

    auto end = std::chrono::steady_clock::now();
    std::chrono::duration<double> elapsed_seconds = end-start;
    std::cout << "elapsed time: " << elapsed_seconds.count() << "s\n";   // solution �Լ�  ���� �ð�

    return 0;
}