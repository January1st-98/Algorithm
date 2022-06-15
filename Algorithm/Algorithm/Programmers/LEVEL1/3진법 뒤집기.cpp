#include <bits/stdc++.h>

using namespace std;

int solution(int n) {
    int answer = 0;
    int tmp = n;
    int index = 0;
    string str = "";
    while(tmp > 0) {
        str += to_string(tmp % 3);
        tmp /= 3;
    }
    reverse(str.begin(), str.end());
    for(int i = 0; i < str.length(); i++) {
        answer += (str[i] - '0') * pow(3, i);
    }
    return answer;
}