#include <bits/stdc++.h>
#include <random>

using namespace std;

/*
특정 노드 방문한 후 네트워크 망에 연결되어 있고 방문하지 않은 노드이면 방문하자
*/

void DFS(int from, int n, vector<int> &visited, vector<vector<int>> &computers)
{

    for (int i = 0; i < n; i++)
    {
        if (from != i && computers[from][i] == 1 && visited[i] == 0)  // 연결되어있고 방문하지 않은 노드라면 방문함
        {
            visited[i] = 1;
            DFS(i, n, visited, computers);
        }
    }
}

int solution(int n, vector<vector<int>> computers)
{

    int network = 0;
    vector<int> visited(n, 0);      // n 개 0으로 초기화

    for (int i = 0; i < n; i++)
    {
        if (visited[i] == 1)       // 방문 했었다면 continue
        {
            continue;
        }

        // visit node and start DFS
        network++;                 // 방문하지 않았다면 카운트하고 방문함                                
        visited[i] = 1;

        DFS(i, n, visited, computers);
    }

    return network;
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

    auto start = std::chrono::steady_clock::now();
    int result = 0;
    result = solution(n, all_network);
    auto end = std::chrono::steady_clock::now();
    std::chrono::duration<double> elapsed_seconds = end - start;
    std::cout << "--- " << elapsed_seconds.count() << " seconds ---\n"; // solution 함수  실행 시간
    cout << "result: " << result << endl;

    return 0;
}