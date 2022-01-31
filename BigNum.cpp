// 큰 수 만들기
#include <iostream>
#include <random>
#include <bits/stdc++.h>

using namespace std;


string solution(string name, int k) {
    string answer = "";
   
    // cout  << name.size() << ' ' << k << endl;
    // name = "4177252841";
    // k = 4;


    // stack 이용
    // 앞에서 부터 담고 뒤에 오는 숫자가 더 크면 앞에꺼랑 비교해서 크면 앞에꺼 버리기 
    // 비교해서 작으면  스택에 추가 
    //  스택이 비어있으면 숫자 추가

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
