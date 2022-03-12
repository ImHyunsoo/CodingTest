#include <bits/stdc++.h>

using namespace std;

int solution(vector<int> money)
{
    int length = money.size();
    int d1[length];
    int d2[length];
    memset(d1, 0, sizeof(d1));
    memset(d2, 0, sizeof(d2));
    d1[0] = d1[1] = money[0];
    d2[1] = money[1];
    for (int i = 2; i < length; i++)
    {
        d1[i] = max(d1[i - 1], d1[i - 2] + money[i]);
        d2[i] = max(d2[i - 1], d2[i - 2] + money[i]);
    }
    return max(d1[length - 2], d2[length - 1]);
}

int main(void)
{
    // cout << solution({1, 2, 3, 1}) << endl;
    cout << solution({10, 2, 2, 100, 2}) << endl;
    return 0;
}