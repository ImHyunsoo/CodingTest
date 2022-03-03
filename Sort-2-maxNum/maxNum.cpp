#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

bool compare(const string &a, const string &b)
{
    if (a + b > b + a)
        return true;
    return false;
}

string solution(vector<int> numbers)
{
    string answer = "";
    vector<string> s_num;
    for (int i = 0; i < numbers.size(); i++)
        s_num.push_back(to_string(numbers[i]));

    sort(s_num.begin(), s_num.end(), compare);

    for (int i = 0; i < s_num.size(); i++)
        answer += s_num[i];
    if (answer[0] == '0')
        return "0";
    return answer;
}

int main()
{
    vector<int> numbers = {6, 10, 2};
    // "6210"
    string result;
    result = solution(numbers);
    cout << result << endl;
    return 0;
}