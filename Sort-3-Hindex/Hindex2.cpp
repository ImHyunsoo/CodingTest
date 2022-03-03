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
    return a < b;
}

int solution(vector<int> citations)
{
    sort(citations.begin(), citations.end(), compare);
    int n = citations.size();
    for (int i = 0; i < n; i++)
    {
        if (citations[i] >= n - i)
            return n - i;
    }
    return 0;
}

int main()
{
    vector<int> citations = {3, 0, 6, 1, 5};
    int result;
    result = solution(citations);
    cout << result << endl;

    return 0;
}