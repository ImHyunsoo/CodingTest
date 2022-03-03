#include <bits/stdc++.h>

using namespace std;

long long solution(int n, vector<int> times)
{
    long long answer = 0;
    long long start = (long long)*min_element(times.begin(), times.end());
    long long end = (long long)*max_element(times.begin(), times.end()) * n;
    int size = times.size();

    while (start <= end)
    {
        long long mid = (start + end) / 2;
        long long total = 0;
        for (int i = 0; i < size; i++)
        {
            total += mid / times[i];
        }
        if (total >= n)
        {
            answer = mid;
            end = mid - 1;
        }
        else
        {
            start = mid + 1;
        }
    }

    return answer;
}

int main(void)
{
    int n;
    vector<int> times;

    cin >> n;
    cin.ignore();
    char str[100], *s;

    // gets(str);
    scanf("%[^\n]", str); // gets_s(str) 와 동일

    for (s = strtok(str, " "); s; s = strtok(NULL, " "))
    {
        int time;
        if (sscanf(s, "%d", &time) < 1)
            break;
        times.push_back(time);
    }

    // n = 6;
    // times = {7, 10};
    // return 28

    int result;
    result = solution(n, times);
    cout << result << endl;

    return 0;
}