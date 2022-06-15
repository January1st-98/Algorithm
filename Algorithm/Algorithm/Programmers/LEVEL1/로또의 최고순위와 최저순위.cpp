#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    vector<int> answer;
    int best = 0;
    int worst = 0;
    for(int i = 0; i < lottos.size(); i++) {
        if(find(win_nums.begin(), win_nums.end(), lottos[i]) != win_nums.end() || lottos[i] == 0) best++;
        if(find(win_nums.begin(), win_nums.end(), lottos[i]) != win_nums.end()) worst++;
    }
    answer.push_back(best == 0  ? 6 : 7 - best);
    answer.push_back(worst == 0 ? 6 : 7 - worst);
    
    
    return answer;
}