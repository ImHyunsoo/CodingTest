#include <bits/stdc++.h>

using namespace std;

/*
큐 (string, int)  노드 단어, 단계 카운트
*/

int solution(string begin, string target, vector<string> words)
{
    queue<pair<string, int>> q; // 큐  (string, int)  노드 단어, 단계 카운트
    q.push(pair<string, int>(begin, 0));
    int size = words.size();

    while (!q.empty())
    {
        pair<string, int> cur;
        cur = q.front();
        q.pop();

        if (cur.first == target) // 타겟에 도달하면 단계 카운트 리턴
            return cur.second;
        if (cur.second > size) // 첫 words 크기보다 크면 타겟 못 찾은거니 0 리턴
            return 0;

        // 다음 노드를 큐에 추가
        for (int i = 0; i < words.size(); i++)
        {
            int cnt = 0;
            for (int j = 0; j < cur.first.size(); j++)
            {
                if (cur.first[j] != words[i][j])
                    cnt++;
            }
            if (cnt == 1)
            {                                                        // 한 글자만 다른 단어들을 찾음
                q.push(pair<string, int>(words[i], cur.second + 1)); // 다음 노드와 단계 카운트를 업데이트하여 큐에 추가
                words.erase(words.begin() + i);                      // words에서 방문한 노드는 제거
            }
        }
    }
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