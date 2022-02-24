#include <bits/stdc++.h>

using namespace std;

/*
visited라는 배열을 활용하는게 신기합니다..
모든 경우를 탐색해 알파벳 순서가 빠른걸로 계속 업데이트 하는 방식이네요
tickets벡터를 정렬해놓고 첫 answer를 바로 리턴하면 시간도 짧게 걸리겠어요

dfs에  int depth 추가
visited[] 를 전역변수로 끌고 나감

if (cur == tickets[i][0] && !visited[i]) // 다음 노드에 해당하면서 방문하지 않았다면
한줄로 표현

string 깊은 복사로 path 업데이트로 인해 내 코드보다(참조자로 path를 pop, push로 끌고 나감) 느림
*/

int visited[10000];
string ans_string = "a";

void dfs(vector<vector<string>> &tickets, string cur, string path, int depth)
{
    if (depth == tickets.size()) // 모든 공항을 거치면 경로가 완성되면
    {
        string p = path;
        if (path < ans_string) // 알파벳 앞선 것으로 ans_string 업데이트 [대소문자 주의]
        {
            ans_string = path;
        }
        return;
    }

    for (int i = 0; i < tickets.size(); i++)
    {
        if (cur == tickets[i][0] && !visited[i]) // 다음 노드에 해당하면서 방문하지 않았다면
        {
            visited[i] = 1;                                               // 해당 노드 방문처리 하고
            dfs(tickets, tickets[i][1], path + tickets[i][1], depth + 1); // 해당 노드 dfs 진입
            visited[i] = 0;                                               // dfs 소멸된 후 해당 노드를 방문하지 않은거로 업데이트
        }                                                                 // 반복문 이어지면 이전 dfs에서 다음 dfs 탐색
                                                                          // 반복문 끝나면  이전 dfs 소멸하고 이전 이전 dfs로 반복
    }
}

vector<string> solution(vector<vector<string>> tickets)
{
    vector<string> answer;
    dfs(tickets, "ICN", "ICN", 0);
    for (int i = 0; i < ans_string.size(); i += 3)
    {
        answer.push_back(ans_string.substr(i, 3));
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
    airport_num = 300;

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