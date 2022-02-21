#include <bits/stdc++.h>
#include <random>

using namespace std;

// [0] +-
// [1] +- +-
// [2] +-+- +-+-
// ...
// 마지막 배열 칸에 최종 합들 나열되어 있음
// 인덱스 하나씩 옮기며 target과 같으면 answer++
int solution(vector<int> numbers, int target)
{
    int answer = 0;
    vector<vector<int>> map(1001);
    map[0].push_back(numbers[0]);
    map[0].push_back(numbers[0] * -1);
    for (int i = 1; i < numbers.size(); i++)
    {
        for (int j = 0; j < map[i - 1].size(); j++)
        {
            map[i].push_back(map[i - 1][j] + numbers[i]);
            map[i].push_back(map[i - 1][j] - numbers[i]);
        }
    }
    for (int i = 0; i < map[numbers.size() - 1].size(); i++)
    {
        if (map[numbers.size() - 1][i] == target)
        {
            answer++;
        }
    }
    return answer;
}

int main(void)
{
    vector<int> numbers;
    int target;
    random_device rd;

    mt19937 gen(rd());

    uniform_int_distribution<int> dis_cnt(2, 20);
    uniform_int_distribution<int> dis_num(1, 50);
    uniform_int_distribution<int> dis_target(1, 1000);

    int n = dis_cnt(gen);
    n = 4;

    for (int i = 0; i < n; i++)
    {
        int number = dis_num(gen);
        numbers.push_back(number);
    }

    target = dis_target(gen);

    cout << "n: " << n << endl;
    cout << "numbers: ";
    for (int i = 0; i < n; i++)
    {
        cout << numbers[i] << ' ';
    }
    cout << endl
         << "target: " << target << endl;

    auto start = std::chrono::steady_clock::now();
    int result = 0;
    result = solution(numbers, target);
    cout << "result: " << result << endl;
    auto end = std::chrono::steady_clock::now();
    std::chrono::duration<double> elapsed_seconds = end - start;
    std::cout << "--- " << elapsed_seconds.count() << " seconds ---\n"; // solution 함수  실행 시간

    return 0;
}