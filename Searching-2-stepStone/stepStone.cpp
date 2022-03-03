#include <bits/stdc++.h>

using namespace std;

int solution(int distance, vector<int> rocks, int n)
{
    int answer = 0;
    long long start = 0, end = distance;

    sort(rocks.begin(), rocks.end());
    rocks.push_back(end);

    while (start <= end)
    {
        long long mid = (start + end) / 2;

        long long offset = 0, last_offset = 0;
        int cnt = 0;
        for (int i = 0; i < rocks.size(); i++)
        {
            offset = rocks[i] - last_offset;
            if (offset < mid)
                cnt++;
            else
                last_offset = rocks[i];
        }
        if (cnt > n)
            end = mid - 1;
        else
        {
            answer = mid;
            start = mid + 1;
        }
    }
    return answer;
}

int main()
{

    cout << solution(25, {2, 14, 11, 21, 17}, 4) << endl;
    return 0;
}