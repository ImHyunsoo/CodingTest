#include <bits/stdc++.h>
#include <random>

using namespace std;

// main과 plusminus가 공유하는 전역변수 설정
int answer_ = 0;
int target_ = 0;

// +++ ... +++
// +++ ... ++-
// +++... +-+
// +++... +--
// +++.. -++
// +++... -+-
// DFS
void plusminus(vector<int> &numbers, int sum)
{
    //탐색 끝났을 경우 조건에 따라 answer++
    if (numbers.size() == 0)
    {
        if (sum == target_)
            answer_++;
        return;
    }
    //더하거나 빼서 재귀
    else
    {
        int tmp = numbers.back();
        numbers.pop_back();
        plusminus(numbers, sum + tmp);
        plusminus(numbers, sum - tmp);
        numbers.push_back(tmp);
    }
}
int solution(vector<int> numbers, int target)
{
    int sum = 0;
    target_ = target;
    plusminus(numbers, sum);
    return answer_;
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
    n = 20;

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