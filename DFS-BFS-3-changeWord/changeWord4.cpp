#include <bits/stdc++.h>

using namespace std;

/*
dfs
visited

// begin  - - -  hot
//     +++  +++ +++  dot
//    -==-  =-=  =--=-       0=-0=-0  =-0=-0-=   =0-0=-0  dog
//    6787606-0=  cog

//  1 + 1  + 1 +1

//  begin answer =  DFS +1
// hot answer =  DFS +1
// dot answer =  DFS +1
// dog answer =  DFS +1
// cog answer =  DFS +1
*/

#define MAX 50

bool visited[MAX];

int DFS(string begin, string target, vector<string> words)
{
    int count = 0;
    int answer = 0;

    for (int i = 0; i < words.size(); ++i)
    {

        if (!visited[i]) // 방문하지 않았으면
        {
            count = 0;
            for (int j = 0; j < words[i].length(); ++j)
            {
                if (begin[j] == words[i][j])
                    ++count;
            }
            if (count == words[i].length() - 1) // 한 글자만 다른 단어이면
            {
                visited[i] = true;   // 방문처리하고
                begin = words[i];    // begin을 그 단어로 업데이트함
                if (begin == target) // 타겟과 같으면  1 리턴
                    return 1;
                else
                    answer += DFS(begin, target, words) + 1; // 타겟과 다르면  dfs 진입, answer 처리, dfs는 0 or 1 리턴
            }
        }
    }

    return answer;
}

int solution(string begin, string target, vector<string> words)
{
    int answer = 0;

    for (int i = 0; i < words.size(); ++i)
    {
        if (words[i] == target) //  words에 타겟이 있으면
        {
            answer = DFS(begin, target, words); // dfs 시작하고 answer를 리턴함
        }
    }

    return answer;
}

int main(void)
{
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> dis_word_len(3, 10);  // 각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같음
    uniform_int_distribution<int> dis_words_num(3, 50); // words에는 3개 이상 50개 이하의 단어가 있으면 중복되는 단어는 없음
    uniform_int_distribution<int> dis_alpha(97, 122);   // 알바벳 소문자

    int word_len = dis_word_len(gen);   // 단어의 길이
    int words_num = dis_words_num(gen); // words안에 단어의 갯수
    // words_num = 50;

    // begin 생성
    string begin = "";
    for (int i = 0; i < word_len; i++)
        begin += char(dis_alpha(gen));
    cout << "begin: " << begin << endl;

    // target 생성 (단, begin과 같지 않음)
    string target = "";
    while (true)
    {
        for (int i = 0; i < word_len; i++)
            target += char(dis_alpha(gen));

        if (target != begin)
            break;
    }
    cout << "target: " << target << endl;

    // words 생성 (중복 없음)
    vector<string> words;
    while (true)
    {
        string word = "";
        for (int j = 0; j < word_len; j++)
        {
            word += char(dis_alpha(gen));
        }
        if (find(words.begin(), words.end(), word) == words.end()) // 중복되는 단어 아님
            words.push_back(word);
        if (words.size() == words_num)
            break;
    }
    cout << "words_num: " << words_num << endl;
    cout << "words: " << endl;
    for (int i = 0; i < words_num; i++)
    {
        cout << words[i] << ' ';
    }
    cout << endl;

    begin = "hit";
    target = "cog";
    words = {"hot", "dot", "dog", "lot", "log", "cog"};

    auto start_time = chrono::steady_clock::now();
    int result = 0;
    result = solution(begin, target, words);
    auto end_time = chrono::steady_clock::now();
    chrono::duration<double> elapsed_seconds = end_time - start_time;
    cout << "--- " << elapsed_seconds.count() << " seconds ---\n";
    cout << "result: " << result << endl;

    return 0;
}