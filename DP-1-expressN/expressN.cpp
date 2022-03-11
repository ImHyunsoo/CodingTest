#include <bits/stdc++.h>

using namespace std;

int solution(int N, int number)
{
    int answer = 0;
    if (number == N)
        return 1;
    vector<vector<int>> d(10, vector<int>(1, -1));
    d[0][0] = 0;
    d[1][0] = N;

    for (int i = 2; i < d.size(); i++)
    {
        vector<int> tmp;
        string s_N = "";
        for (int j = 0; j < i; j++)
            s_N += to_string(N);
        tmp.push_back(stoi(s_N));
        for (int j = 1; j <= i / 2; j++)
            for (int k = 0; k < d[j].size(); k++)
                for (int l = 0; l < d[i - j].size(); l++)
                {
                    tmp.push_back(d[j][k] * d[i - j][l]);
                    tmp.push_back(d[j][k] + d[i - j][l]);
                    if (d[i - j][l] != 0)
                        tmp.push_back(d[j][k] / d[i - j][l]);
                    if (d[j][k] != 0)
                        tmp.push_back(d[i - j][l] / d[j][k]);
                    tmp.push_back(d[j][k] - d[i - j][l]);
                    tmp.push_back(d[i - j][l] - d[j][k]);
                }
        tmp.erase(unique(tmp.begin(), tmp.end()), tmp.end());
        d[i] = tmp;
        for (int m = 0; m < d[i].size(); m++)
            if (d[i][m] == number)
                return i;
    }

    return -1;
}

int main(void)
{
    int N = 5, number = 12;

    cout << solution(N, number) << endl;

    return 0;
}