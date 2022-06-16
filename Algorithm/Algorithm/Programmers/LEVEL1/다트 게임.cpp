#include <bits/stdc++.h>

using namespace std;

int power(int num, int time) {
    int result = 1;
    for(int i = 0; i < time; i++) {
        result = result * num;
    }
    return result;
}

int solution(string dartResult) {
    int answer = 0;
    vector<int> result;

    int num = 0;
    for(char ch: dartResult) {
        if(ch >= '0' && ch <= '9') {
            num *= 10;
            num += ch - '0';
        }
        else if(ch == 'S' || ch == 'D' || ch == 'T') {
            if(ch == 'S') {
                num = power(num, 1);
            } else if(ch == 'D') {
                num = power(num, 2);
            } else if(ch == 'T') {
                num = power(num, 3);
            }
            result.push_back(num);
            num = 0;
        }
        else if(ch == '*') {
            if(result.size() == 1) {
                result[0] = result[0] * 2;
            } 
            else if(result.size() >= 2) {
                result[result.size() - 1] = result[result.size() - 1] * 2;
                result[result.size() - 2] = result[result.size() - 2] * 2;
            }
        } 
        else if(ch == '#') {
            result[result.size()-1] = -result[result.size()-1];
        }
    }

    for(auto num: result) {
        answer += num;
    }
    return answer;
}