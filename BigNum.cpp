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
