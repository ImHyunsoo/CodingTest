#include <bits/stdc++.h>
#include <random>

using namespace std;

bool promising(int depth, const vector<int> &numbers, int search, int target) {
    int lastSum = 0;
    for (int i = depth; i < numbers.size(); i++) {
        lastSum += numbers[i];
    }

    if (search + lastSum < target || search - lastSum > target) {
        return false;
    }
    else return true;
}

void searchNum(int &answer, int depth, const vector<int> &numbers, int search, int target) {
    if (promising(depth, numbers, search, target)) {
        if (depth == numbers.size()) {
            answer++;
            return;
        }

        search += numbers[depth];
        searchNum(answer, depth + 1, numbers, search, target);

        search -= (2 * numbers[depth]);
        searchNum(answer, depth + 1, numbers, search, target);
    }
}

int solution(vector<int> numbers, int target) {

    int answer = 0;

    searchNum(answer, 0, numbers, 0, target);

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