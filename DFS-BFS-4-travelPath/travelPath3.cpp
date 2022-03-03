#include <bits/stdc++.h>

using namespace std;

/*
티켓들을 정렬하고  첫 번째 경로를 찾으면 바로 리턴
10000번도 처리 가능

노드를 dfs로 방문하는데 방문할데가 없으면 리턴하고 스택에 추가
<생소하지만 매우 빠름>
dfs 깊은 곳에서부터 스택에 차례로 넣고  탐색할 dfs 있으면 탐색 후 가장 깊은 곳에서부터 스택에 차례로 넣음


방문하지 않고 다음 노드에 해당하면 방문처리하고 dfs 탐색
더 이상 dfs 들어갈 곳이 없다면 리턴

이전 dfs가 소멸하는 과정에 먼저 스택에 마지막 노드 추가함
다른 다음 dfs를 탐색하고
더 이상 dfs 들어갈 곳이 없다면 리턴
이것을 반복


*/

stack<string> st;

// 맨 아래에 마지막 공항이, 맨 위에 첫 공항이오도록 스택 쌓임
int DFS(vector<vector<string>> &tickets, vector<bool> &visited, string start)
{
    for (int i = 0; i < tickets.size(); ++i)
    {
        if (!visited[i])
        {
            if (tickets[i][0] == start)
            {
                visited[i] = true;
                DFS(tickets, visited, tickets[i][1]); // 알파벳 앞선 다음 도착지만 찾아나가면 무조건 모든 경로 거칠 수 있나? 아님
                st.push(tickets[i][1]);
            }
        }
    }
    return 0;
}

bool compare(vector<string> a, vector<string> b)
{
    return a[1] < b[1];
}

vector<string> solution(vector<vector<string>> tickets)
{
    vector<string> answer;
    vector<bool> visited;

    for (int i = 0; i < tickets.size(); ++i)
        visited.push_back(false);

    sort(tickets.begin(), tickets.end(), compare); // 티켓의 도착지를 기준으로 오름차순 정렬

    cout << "tickets: ";
    for (int i = 0; i < tickets.size(); i++)
    {
        cout << "{" << tickets[i][0] << ", " << tickets[i][1] << "}" << ' ';
    }
    cout << endl;

    // DFS(tickets, visited, "ICN");
    DFS(tickets, visited, "a");

    // answer.push_back("ICN");
    answer.push_back("a");
    while (!st.empty())
    {
        answer.push_back(st.top());
        st.pop();
    }

    return answer;
}

int main(void)
{
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> dis_airport_num(3, 10000); // 주어진 공항 수는 3개 이상 10,000개 이하
    uniform_int_distribution<int> dis_alphabet(65, 90);      // 'A' ~ 'Z'

    int airport_num = dis_airport_num(gen);
    airport_num = 10000;

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
    tickets = {{"a", "g"}, {"g", "h"}, {"h", "i"}, {"i", "j"}, {"j", "e"}, {"e", "f"}, {"a", "w"}, {"w", "a"}};

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
    cout << result.size() << ' ';
    cout << "result: ";
    for (int i = 0; i < result.size(); i++)
    {
        cout << result[i] << " ";
    }
    cout << endl;

    return 0;
}