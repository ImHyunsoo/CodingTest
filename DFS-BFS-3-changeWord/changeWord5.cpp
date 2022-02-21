#include <bits/stdc++.h>

using namespace std;

/*
dfs
visited

다음 노드를 찾이 못하면 dfs 진입 못함
dfs  카운트하면서 탐색
타겟 찾았을 때 최소 answer 가 반환 되도록 함
*/

string targ;
vector<string> word;
int size1;
int wordsize;
int answer;

void bfs(int n, string begin, vector<int> visited)
{
    if (begin.compare(targ) == 0 && n < answer) // compare 같으면 0 리턴,  다르면 -1 리턴
        answer = n;
    for (int i = 0; i < size1; i++)
    {
        if (visited[i] == 1)
            continue; // 방문 했으면 continue
        int t = 0;
        for (int j = 0; j < wordsize; j++)
        {
            if (begin[j] != word[i][j])
                t++; // 두 글자 이상 틀리면 break
            if (t > 1)
                break;
        }
        if (t == 1)
        {
            visited[i] = 1; // 한 글자 다르면 방문처리하고 dfs 진입,  카운트함, 다음 노드, 방문 넘김
            bfs(n + 1, word[i], visited);
        }
    }
}

int solution(string begin, string target, vector<string> words)
{
    answer = 999999999;
    size1 = words.size();
    wordsize = begin.length();
    targ = target;
    word = words;
    vector<int> visited(size1, 0);
    bfs(0, begin, visited);
    if (answer == 999999999)
        return 0;
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