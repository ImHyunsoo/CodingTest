#include <bits/stdc++.h>
#include <random>

using namespace std;

// int visited2[201][201];

/*
특정 노드 방문한 후 네트워크 망에 연결되어 있고 방문하지 않은 노드이면 방문하자
*/

void dfs(vector<vector<int>> &computers, int node, int visited3[])
{
    visited3[node] = 1;
    for (int i = 0; i < computers[node].size(); i++)
    {
        if (computers[node][i] == 1 && visited3[i] == 0)
            dfs(computers, i, visited3);
    }
}

int solution(int n, vector<vector<int>> computers)
{
    int answer = 0;
    int visited3[201];
    memset(visited3, 0, sizeof(visited3));
    // cout << "sizeof(visited3): " << sizeof(visited3) << endl;

    // for (int i = 0; i < n; i++)
    // {
    //     cout << visited3[i] << ' ';
    // }

    for (int i = 0; i < n; i++)
    {
        if (!visited3[i])
        {
            dfs(computers, i, visited3);
            answer++;
        }
    }

    return answer;
}

int main(void)
{
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> com_cnt(1, 200); // 컴퓨터의 개수 n은 1 이상 200 이하인 자연수
    uniform_int_distribution<int> b_con(0, 1);     // 연결 여부 0, 1

    int n = com_cnt(gen);
    n = 200;

    // memset(visited2, 0, sizeof(visited2));
    // cout << "visited2: " << endl;
    // for (int i = 0; i < n; i++)
    // {
    //     for (int j = 0; j < n; j++)
    //     {
    //         cout << visited2[i][j] << ' ';
    //     }
    //     cout << endl;
    // }
    // cout << endl;

    // cout << "visited1: " << endl;
    int visited1[n][n] = {};
    // for (int j = 0; j < n; j++)
    // {
    //     for (int i = 0; i < n; i++)
    //     {
    //         cout << visited1[j][i] << ' ';
    //     }
    //     cout << endl;
    // }
    // cout << endl;

    vector<vector<int>> all_network;
    for (int j = 0; j < n; j++)
    {
        vector<int> node_network;
        for (int i = 0; i < n; i++)
        {
            if (visited1[j][i] == 0)
            { // 방문하지 않았다면 방문하자
                visited1[j][i] = 1;
                if (j < i)
                { //  0, 1 중 랜덤 숫자 추가
                    node_network.push_back(b_con(gen));
                }
                else if (j == i)
                { //  1 추가
                    node_network.push_back(1);
                }
                else
                { // j -> i  ==  i -> j 므로  이전 값 추가
                    node_network.push_back(all_network[i][j]);
                }
            }
        }
        all_network.push_back(node_network);
    }

    // cout << "all_network: " << endl;
    // for (int j = 0; j < n; j++)
    // {
    //     for (int i = 0; i < n; i++)
    //     {
    //         cout << all_network[j][i] << ' ';
    //     }
    //     cout << endl;
    // }

    auto start = std::chrono::steady_clock::now();
    int result = 0;
    result = solution(n, all_network);
    auto end = std::chrono::steady_clock::now();
    std::chrono::duration<double> elapsed_seconds = end - start;
    std::cout << "--- " << elapsed_seconds.count() << " seconds ---\n"; // solution 함수  실행 시간
    cout << "result: " << result << endl;

    return 0;
}