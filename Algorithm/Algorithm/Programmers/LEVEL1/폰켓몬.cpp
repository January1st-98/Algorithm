#include <bits/stdc++.h>
using namespace std;

int solution(vector<int> nums)
{
    int answer = 0;
    int N = nums.size() / 2;
    set<int> s;
    for(auto num: nums) {
        s.insert(num);
    }
    if(s.size() <= N) { answer = s.size(); }
    else { answer = N; }
    
    return answer;
}