// ū �� �����
#include <iostream>
#include <random>
#include <bits/stdc++.h>

using namespace std;


string solution(string name, int k) {
    string answer = "";
   
    // cout  << name.size() << ' ' << k << endl;
    // name = "4177252841";
    // k = 4;


    // stack �̿�
    // �տ��� ���� ��� �ڿ� ���� ���ڰ� �� ũ�� �տ����� ���ؼ� ũ�� �տ��� ������ 
    // ���ؼ� ������  ���ÿ� �߰� 
    //  ������ ��������� ���� �߰�

    vector<int> my_stack;
    my_stack.push_back(name[0] - '0');
    for (int i = 1; i < name.size(); i++) {
        while (my_stack.size() > 0 && k > 0 && my_stack.back() < name[i] -'0') {
            my_stack.pop_back();
            k--;      
        } 
        my_stack.push_back(name[i]-'0');
    }

  
    for (int i = 0; i < my_stack.size()-k; i++) {
        answer += my_stack[i] + '0';
    }

    // cout << "answer: " << answer << endl;
    
    return answer;
}


int main() {
    random_device rd;

    // random_device �� ���� ���� ���� ������ �ʱ�ȭ �Ѵ�.
    mt19937 gen(rd());
    // mt19937 gen(123);

    // 0 ���� 99 ���� �յ��ϰ� ��Ÿ���� �������� �����ϱ� ���� �յ� ���� ����.
    // uniform_int_distribution<int> dis(0, 99);
    uniform_int_distribution<int> dis_num_len(1, 1000000);

    int number_len = dis_num_len(gen);
    // number_len = 999999;

    uniform_int_distribution<int> dis_remove_len(1, number_len-1);   // ���ڿ� ����
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
