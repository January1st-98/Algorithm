#include <bits/stdc++.h>

using namespace std;
int i;
bool cmp(string a, string b) {
    if(a[i] == b[i]) {
        int length = min(a.length(), b.length());
        for(int i = 0; i < length; i++) {
            if(a[i] == b[i]) continue;
            if(a[i] < b[i]) return true;
            else return false;
        }
    } else {
        return a[i] < b[i];
    }
}

vector<string> solution(vector<string> strings, int n) {
    vector<string> answer(strings);
    i = n;
    sort(answer.begin(), answer.end(), cmp);
    return answer;
}