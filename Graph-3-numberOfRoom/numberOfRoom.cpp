#include <bits/stdc++.h>

using namespace std;

int solution(vector<int> arrows)
{
    int answer = 0;

    vector<pair<int, int>> move = {{-2, 0}, {-2, 2}, {0, 2}, {2, 2}, {2, 0}, {2, -2}, {0, -2}, {-2, -2}};

    map<pair<pair<int, int>, pair<int, int>>, bool> road;
    map<pair<int, int>, bool> node_visited;
    pair<int, int> now = {0, 0};
    pair<int, int> next;
    queue<pair<int, int>> q;

    // 노드 큐에 넣고, road 방문 처리
    node_visited.insert({now, false});
    q.push(now);
    for (int i = 0; i < arrows.size(); i++)
    {
        for (int j = 0; j < 2; j++)
        {
            next.first = now.first + move[arrows[i]].first / 2;
            next.second = now.second + move[arrows[i]].second / 2;
            q.push(next);
            node_visited.insert({next, false});
            road.insert({{now, next}, false});
            road.insert({{next, now}, false});
            now = next;
        }
    }

    now.first = q.front().first;
    now.second = q.front().second;
    q.pop();
    node_visited[now] = true;
    while (!q.empty())
    {
        next.first = q.front().first;
        next.second = q.front().second;
        q.pop();
        if (node_visited[next] == true && road[{next, now}] == false)
            answer++;
        else
            node_visited[next] = true;
        road[{now, next}] = true;
        road[{next, now}] = true;
        now = next;
    }

    return answer;
}

int main()
{
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> dis(0, 7);

    vector<int> arrows(100000);
    for (int i = 0; i < 100000; i++)
    {
        arrows[i] = dis(gen);
    }

    // vector<int> arrows = {6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0};

    auto start_time = chrono::steady_clock::now();

    cout << solution(arrows) << endl;

    auto end_time = chrono::steady_clock::now();
    chrono::duration<double> elapsed_seconds = end_time - start_time;
    cout << "--- " << elapsed_seconds.count() << " seconds ---" << endl;
    return 0;
}
