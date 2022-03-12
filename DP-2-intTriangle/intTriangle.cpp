#include <bits/stdc++.h>

using namespace std;
// 프로그래머스에서 어떤 문제는 함수인자에 &을 빼야 통과함 (dfs/bfs 문제에서는 & 통과했는데 몇몇 문제에서 & 빼야 통과함)
int solution(vector<vector<int>> &triangle)
{
    for (int i = 1; i < triangle.size(); i++)
    {
        for (int j = 0; j < triangle[i].size(); j++)
        {
            if (j == 0)
                triangle[i][0] += triangle[i - 1][0];
            else if (j == i)
                triangle[i][j] += triangle[i - 1][j - 1];
            else
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j]);
        }
    }
    int max_value = -1;
    for (int j = 0; j < triangle[triangle.size() - 1].size(); j++)
        if (max_value < triangle[triangle.size() - 1][j])
            max_value = triangle[triangle.size() - 1][j];
    return max_value;
}

int main(void)
{
    vector<vector<int>> triangle = {{7}, {3, 8}, {8, 1, 0}, {2, 7, 4, 4}, {4, 5, 2, 6, 5}};
    cout << solution(triangle) << endl;
    return 0;
}