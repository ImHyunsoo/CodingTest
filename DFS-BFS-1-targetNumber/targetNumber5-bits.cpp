#include <bits/stdc++.h>
#include <random>

using namespace std;

int solution(vector<int> numbers, int target)
{
    int answer = 0;
    int size = 1 << numbers.size();
    cout << "size: " << bitset<24>(size) << endl;

    /*
    + + + + ...
    - + + + ...
    + - + + ...
    - - + + ...
    + + - + ...
    - + - + ...
    - - - + ...
    ...
    */

    for (int i = 0; i < size; i++)
    {
        int temp = 0;
        for (int j = 0; j < numbers.size(); j++)
        {
            if (i & (1 << j))
            {
                temp -= numbers[j];
            }
            else
                temp += numbers[j];
        }
        if (temp == target)
            answer++;
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