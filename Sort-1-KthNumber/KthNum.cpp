#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands)
{
    vector<int> answer;
    for (int i = 0; i < commands.size(); i++)
    {
        vector<int> cut_array(commands[i][1] - (commands[i][0] - 1));
        copy(array.begin() + commands[i][0] - 1, array.begin() + commands[i][1], cut_array.begin());
        sort(cut_array.begin(), cut_array.end());
        answer.push_back(cut_array[commands[i][2] - 1]);
    }
    return answer;
}