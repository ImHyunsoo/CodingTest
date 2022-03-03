#include <bits/stdc++.h>

using namespace std;

/*
// 방문 처리
// 다음 노드들에 대해 방문 하지 않았다면 dfs 방문함

vector<bool> visited(n, 0); // 방문처리 초기화 // 1차원 배열 말고 vector 이용하면 디버깅할 때 값 보기 편함

알파벳 순으로 티겟 정렬

// 최종 경로가 완성되면 paths에 path 추가함

다음 노드들에 대해
    방문하지 않았다면
        dfs 탐색
(참조자로 visited 끌고가며 업데이트)
(path도 끌고가며 업데이트)

해당 dfs 재귀가 소멸하는 과정에서 반복문이 반복되며 다른 다음 노드로 진입할 수도 있고
반복이 끝났다면  visited[v] = false;  path.pop_back(); 업데이트하고  소멸됨
*/

vector<vector<string>> paths;

void dfs(vector<vector<string>> &tickets, vector<bool> &visited, int v, string fr, vector<string> &path)
{
    // 최종 경로가 완성되면
    if (path.size() == tickets.size() + 1)
    {
        paths.push_back(path);
        visited[v] = false;
        path.pop_back();
        return;
    }

    // 다음 노드들에 대해
    for (int i = 0; i < tickets.size(); i++)
    {
        if (fr == tickets[i][0])
        {
            // 방문하지 않았다면
            if (!visited[i])
            {
                visited[i] = true;
                path.push_back(tickets[i][1]);
                dfs(tickets, visited, i, tickets[i][1], path);
            }
        }
    }
    // 방문할 다음 노드가 없으므로
    visited[v] = false;
    path.pop_back();
}

vector<string> solution(vector<vector<string>> tickets)
{
    int n = tickets.size();
    vector<bool> visited(n, 0); // 방문처리 초기화 // 1차원 배열 말고 vector 이용하면 디버깅할 때 값 보기 편함

    sort(tickets.begin(), tickets.end()); // 알파벳 순으로 티겟 정렬

    vector<string> path;
    path.push_back("ICN");
    dfs(tickets, visited, 0, "ICN", path);

    return paths[0];
}

int main(void)
{
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> dis_airport_num(3, 10000); // 주어진 공항 수는 3개 이상 10,000개 이하
    uniform_int_distribution<int> dis_alphabet(65, 90);      // 'A' ~ 'Z'

    int airport_num = dis_airport_num(gen);
    airport_num = 800;

    string fr = "ICN";
    vector<vector<string>> tickets;
    for (int i = 0; i < airport_num; i++)
    {
        vector<string> ticket;
        string to = "";
        ticket.push_back(fr);
        for (int j = 0; j < 3; j++)
        {
            to += char(dis_alphabet(gen));
        }
        if (fr != to) // 티켓의 출발지와 도착지가 달라지도록 처리
        {
            ticket.push_back(to);
            fr = to;
            tickets.push_back(ticket);
        }
        else
            i--;
    }

    shuffle(tickets.begin(), tickets.end(), gen); // 배열의 순서를 랜덤으로 셔플

    // tickets = {{"ICN", "SFO"}, {"ICN", "ATL"}, {"SFO", "ATL"}, {"ATL", "ICN"}, {"ATL", "SFO"}};

    // cout << "tickets: ";
    // for (int i = 0; i < tickets.size(); i++)
    // {
    //     cout << "{" << tickets[i][0] << ", " << tickets[i][1] << "}" << ' ';
    // }
    // cout << endl;

    vector<string> result;
    auto start_time = chrono::steady_clock::now();

    result = solution(tickets);

    auto end_time = chrono::steady_clock::now();
    chrono::duration<double> elapsed_seconds = end_time - start_time;
    cout << "--- " << elapsed_seconds.count() << " seconds ---" << endl;
    cout << "result: ";
    for (int i = 0; i < result.size(); i++)
    {
        cout << result[i] << " ";
    }
    cout << endl;

    return 0;
}