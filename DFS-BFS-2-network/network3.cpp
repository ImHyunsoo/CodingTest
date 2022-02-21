#include <bits/stdc++.h>
#include <random>
#define MAX 200

using namespace std;

/*
특정 노드 방문한 후 네트워크 망에 연결되어 있고 방문하지 않은 노드이면 방문하자
*/

bool visitied[MAX]; // 전역 visited,  MAX 만큼 0으로 초기화

int DFS(vector<vector<int>> &computers, vector<int> &numbers, int n)
{
    visitied[n] = true;

    for (int i = 0; i < numbers.size(); ++i)
    {
        if (!visitied[i] && numbers[i] == 1) // i노드와 연결되어 있고 그 노드를 방문하지 않았다면  방문함
            DFS(computers, computers[i], i);
    }

    return 0;
}

int solution(int n, vector<vector<int>> computers)
{
    int answer = 0;

    for (int i = 0; i < n; ++i)
    {
        if (!visitied[i]) // 방문하지 않았다면 방문함
        {
            DFS(computers, computers[i], i);
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