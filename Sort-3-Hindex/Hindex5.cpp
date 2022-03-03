#include <bits/stdc++.h>

using namespace std;

void print(vector<int> citations)
{
    for (int i = 0; i < citations.size(); i++)
        cout << citations[i] << ' ';
    cout << endl;
}

bool compare(const int &a, const int &b)
{
    return a > b;
}

int solution(vector<int> citations)
{
    int answer = 0;
    sort(citations.begin(), citations.end(), ::greater<int>());
    for (int i = 0; i < citations[0]; i++)
    {
        int count = 0;
        for (int j = 0; j <= i; j++)
        {
            if (i + 1 <= citations[j])
                count++;
        }
        if (i + 1 == count)
            answer = count;
    }
    return answer;
}

int main()
{
    vector<int> citations = {3, 0, 6, 1, 5};
    int result;
    result = solution(citations);
    cout << result << endl;

    return 0;
}