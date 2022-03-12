#include <bits/stdc++.h>

using namespace std;

int solution(int m, int n, vector<vector<int>> puddles)
{
    long long d[n + 1][m + 1];
    memset(d, 0, sizeof(d));
    d[0][1] = 1;

    for (int k = 0; k < puddles.size(); k++)
    {
        d[puddles[k][1]][puddles[k][0]] = -1;
    }

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            if (d[i][j] == -1)
                d[i][j] = 0;
            else
                d[i][j] = (d[i - 1][j] + d[i][j - 1]) % 1000000007;
        }
    }
    return d[n][m];
}

int main()
{
    // return 4
    // cout << solution(4, 3, {{2, 2}}) << endl;
    cout << solution(100, 100, {{2, 2}}) << endl;
    // cout << solution(4, 3, {{2, 2}}) << endl;

    return 0;
}