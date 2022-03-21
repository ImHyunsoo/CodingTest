// #include <string>
// #include <vector>
// #include <map>
#include <bits/stdc++.h>

using namespace std;

int dx[] = {-1, -1, 0, 1, 1, 1, 0, -1};
int dy[] = {0, 1, 1, 1, 0, -1, -1, -1};

int solution(vector<int> arrows)
{
    map<pair<int, int>, bool> Node_Visit;
    map<pair<pair<int, int>, pair<int, int>>, bool> Edge_Visit;

    int answer = 0;
    int x = 0;
    int y = 0;
    Node_Visit[{x, y}] = true;
    for (int i = 0; i < arrows.size(); i++)
    {
        int dir = arrows[i];
        for (int j = 0; j < 2; j++)
        {
            int nx = x + dx[dir];
            int ny = y + dy[dir];

            if (Node_Visit[{nx, ny}] == true && Edge_Visit[{{x, y}, {nx, ny}}] == false)
            {
                Edge_Visit[{{x, y}, {nx, ny}}] = true;
                Edge_Visit[{{nx, ny}, {x, y}}] = true;
                answer++;
                x = nx;
                y = ny;
                continue;
            }

            Node_Visit[{nx, ny}] = true;
            Edge_Visit[{{x, y}, {nx, ny}}] = true;
            Edge_Visit[{{nx, ny}, {x, y}}] = true;
            x = nx;
            y = ny;
        }
    }
    return answer;
}

int main()
{
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> dis(0, 7);

    // vector<int> arrows(100000);
    // for (int i = 0; i < 100000; i++)
    // {
    //     arrows[i] = dis(gen);
    // }

    vector<int> arrows = {6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0};

    auto start_time = chrono::steady_clock::now();

    cout << solution(arrows) << endl;

    auto end_time = chrono::steady_clock::now();
    chrono::duration<double> elapsed_seconds = end_time - start_time;
    cout << "--- " << elapsed_seconds.count() << " seconds ---" << endl;
    return 0;
}
