#include <bits/stdc++.h>
#define INF 1e9
#define WIN 1
#define LOSE -1

using namespace std;

int solution(int n, vector<vector<int>> results)
{
    int answer = 0;
    int graph[n + 1][n + 1];

    for (int i = 0; i <= n; i++)
    {
        fill(graph[i], graph[i] + (n + 1), INF);
        graph[i][i] = 0;
    }

    for (int i = 0; i < results.size(); i++)
    {
        graph[results[i][0]][results[i][1]] = WIN;
        graph[results[i][1]][results[i][0]] = LOSE;
    }

    for (int k = 1; k <= n; k++)
    {
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                if (graph[i][k] == WIN && graph[k][j] == WIN)
                {
                    graph[i][j] = WIN;
                    graph[j][i] = LOSE;
                }
            }
        }
    }

    for (int i = 1; i <= n; i++)
    {
        int cnt = 0;
        for (int j = 1; j <= n; j++)
        {
            if (graph[i][j] == 1 || graph[i][j] == -1)
                cnt++;
        }
        if (cnt == n - 1)
            answer++;
    }

    return answer;
}

int main()
{
    int n = 5;
    vector<vector<int>> results = {{4, 3}, {4, 2}, {3, 2}, {1, 2}, {2, 5}};
    cout << solution(n, results) << endl;
    return 0;
}