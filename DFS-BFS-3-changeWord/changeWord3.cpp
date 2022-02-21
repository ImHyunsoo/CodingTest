#include <bits/stdc++.h>

using namespace std;

/*
큐 (string, int)
visited[]
*/
int visited[50];

int possible(string a, string b)
{
    int i;
    int cnt = 0;

    for (i = 0; i < a.length(); i++)
    {
        if (a[i] != b[i])
            cnt++;
    }

    if (cnt == 1)
        return 1;
    else
        return 0;
}

int solution(string begin, string target, vector<string> words)
{
    int answer = 0;
    queue<pair<string, int>> Q;
    int i;
    string temp;
    int num;

    Q.push(make_pair(begin, 0));
    while (!Q.empty())
    {
        temp = Q.front().first;
        num = Q.front().second;
        Q.pop();

        if (temp.compare(target) == 0)
        {
            answer = num;
            break;
        }

        for (i = 0; i < words.size(); i++)
        {
            if (visited[i])
                continue;
            if (possible(temp, words[i]))
            {
                visited[i] = 1;
                Q.push(make_pair(words[i], num + 1));
            }
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