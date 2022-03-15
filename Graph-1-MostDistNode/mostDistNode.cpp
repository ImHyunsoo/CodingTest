#include <bits/stdc++.h>
#define INF 1e9

using namespace std;

int solution(int n, vector<vector<int>> edge)
{
    int distance[n + 1];
    fill(distance, distance + (n + 1), INF);

    vector<pair<int, int>> graph[n + 1];
    for (int i = 0; i < edge.size(); i++)
    {
        graph[edge[i][0]].push_back({edge[i][1], 1});
        graph[edge[i][1]].push_back({edge[i][0], 1});
    }

    int start = 1;
    priority_queue<pair<int, int>> pq;
    pq.push({0, start});
    distance[start] = 0;
    while (!pq.empty())
    {
        int dist = -pq.top().first;
        int now = pq.top().second;
        pq.pop();
        if (distance[now] < dist)
            continue;
        for (int i = 0; i < graph[now].size(); i++)
        {
            int cost = dist + graph[now][i].second;
            if (cost < distance[graph[now][i].first])
            {
                distance[graph[now][i].first] = cost;
                pq.push({-cost, graph[now][i].first});
            }
        }
    }

    int max_dist = 0;
    for (int i = 1; i < n + 1; i++)
    {
        if (distance[i] == INF)
            continue;
        if (max_dist < distance[i])
            max_dist = distance[i];
    }
    int cnt = 0;
    for (int i = 1; i < n + 1; i++)
    {
        if (max_dist == distance[i])
            cnt++;
    }
    return cnt;
}

int main(void)
{
    int n = 6;
    vector<vector<int>> edge = {{3, 6}, {4, 3}, {3, 2}, {1, 3}, {1, 2}, {2, 4}, {5, 2}};
    cout << solution(n, edge) << endl;
    return 0;
}