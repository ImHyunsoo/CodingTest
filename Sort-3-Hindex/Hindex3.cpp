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
    sort(citations.begin(), citations.end(), greater<int>());
    print(citations);
    for (int i = 0; i < citations.size(); ++i)
    {
        if (citations[i] < i + 1)
        {
            return i;
        }
    }

    return citations.size();
}

int main()
{
    vector<int> citations = {3, 0, 6, 1, 5};
    int result;
    result = solution(citations);
    cout << result << endl;

    return 0;
}