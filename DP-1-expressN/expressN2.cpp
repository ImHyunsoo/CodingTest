#include <string>
#include <vector>
#include <iostream>

using namespace std;

int minCnt = 9;

// dfs 탐색
// 모든 사칙 연산 고려

void dp(int N, int number, int cnt, int now)
{
    if (cnt > 8)
    {
        return;
    }

    if (now == number)
    {
        minCnt = min(minCnt, cnt);
    }

    int operand = 0;

    for (int i = 1; i <= 9; i++)
    {
        // 5, 55, 555 만들기
        operand = operand * 10 + N;

        dp(N, number, cnt + i, now + operand);
        dp(N, number, cnt + i, now - operand);

        if (now != 0)
        {
            dp(N, number, cnt + i, now * operand);
            dp(N, number, cnt + i, now / operand);
        }
    }
}
int solution(int N, int number)
{
    int answer = 0;
    dp(N, number, 0, 0);
    answer = ((minCnt > 8) ? -1 : minCnt);
    return answer;
}

int main()
{
    cout << solution(5, 12) << endl;
    return 0;
}