#include <bits/stdc++.h>

using namespace std;

bool cmp(pair<double, int> a, pair<double, int> b) {
    if(a.first == b.first) { return a.second < b.second; }
    else { return a.first > b.first; }
}

vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;
    vector<pair<double, int>> fail;
    
    for(int i = 1; i <= N; i++) {
        int cur = i;
        int cur_clear = 0;
        int cur_fail = 0;
        for(int j = 0; j < stages.size(); j++) {
            if(stages[j] >= cur) cur_clear++;
            if(stages[j] == cur) cur_fail++;
        }
        if(cur_clear == 0) fail.push_back({0, cur});
        else {
            double fail_rate = (double)cur_fail / (double)cur_clear;
            fail.push_back({fail_rate, cur});
        }
    }
    sort(fail.begin(), fail.end(), cmp);
    for(auto result: fail) { answer.push_back(result.second); }
    
    return answer;
}