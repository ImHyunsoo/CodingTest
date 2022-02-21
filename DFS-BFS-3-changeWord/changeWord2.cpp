#include <bits/stdc++.h>

using namespace std;

/*
큐 (string)
한 글자 다른 단어 찾기
q_step
next_q_step 큐를 활용
*/

// 한 글자만 다른 단어들을 찾아서 words 에서 제거하고 큐에 추가해서 큐를 리턴
queue<string> OneLetterDiff(string node, vector<string> &words)
{
    queue<string> q;

    for (int i = 0; i < words.size(); i++)
    {
        int cnt = 0;
        for (int j = 0; j < node.size(); j++) // 한 글자씩 비교해서 다르면 카운트
        {
            if (node[j] != words[i][j])
                cnt++;
        }
        if (cnt == 1) // 한 글자만 다른 경우
        {
            q.push(words[i]);
            words.erase(words.begin() + i);
        }
    }

    return q;
}

int solution(string begin, string target, vector<string> words)
{
    int answer = 0;
    queue<string> q_step;
    queue<string> q_next_step;
    q_step.push(begin);

    while (true)
    {
        //현 스탭 노드들에 대하여 다음 스탭 노드들을 찾음
        while (!q_step.empty())
        {
            string node;
            node = q_step.front();
            q_step.pop();

            if (node == target) // 타겟에 도달하면 찾기에 성공한 것이므로 answer 리턴
                return answer;

            // 다음 스탭 노드들을 찾아서 큐에 추가 (한 글자 다른 것이 다음 노드임)
            q_next_step = OneLetterDiff(node, words);
        }

        if (q_next_step.empty()) // 다음 스탭이 비어 있으면 타켓 찾기 실패이므로 0 리턴
            return 0;
        q_step = q_next_step; // 다음 스탭을 업데이트
        answer++;             //  다음 스탭으로 가면서 카운트
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