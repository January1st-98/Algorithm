#include <bits/stdc++.h>

using namespace std;

bool cmp(pair<string, int>& a, pair<string, int>& b) {
    return a.second < b.second;
}

vector<string> solution(vector<string> orders, vector<int> course) {
    vector<string> answer;
    for(string &order: orders) sort(order.begin(), order.end());
    for(auto c: course) {
        map<string, int> m;
        for(auto order: orders) {
            if(order.length() > c) {
                vector<int> comb(order.length()-c, 0);
                for(int i = 0; i < c; i++) { comb.push_back(1); }
                do {
                    string tmp = "";
                    for(int i = 0; i < order.length(); i++) {
                        if(comb[i] == 0) continue;
                        tmp += order[i];
                    }
                    m[tmp]++;
                } while(next_permutation(comb.begin(), comb.end()));
            }
            else if(order.length() == c) { m[order]++; }
        }
        int max_value = -1;
        for(auto iter: m) {
            if(iter.second > max_value) max_value = iter.second;
        }
        if(max_value < 2) continue;
        for(auto iter: m) {
            if(iter.second == max_value) {
                answer.push_back(iter.first);
            }
        }
    }
    sort(answer.begin(), answer.end());
    
    return answer;
}