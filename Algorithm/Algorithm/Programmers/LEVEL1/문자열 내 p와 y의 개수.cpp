#include <string>
#include <iostream>
using namespace std;

bool solution(string s)
{
    bool answer = true;
    int num = 0;
    for(auto ch: s) {
        if(ch == 'p' || ch == 'P') num++;
        else if(ch == 'y'|| ch == 'Y') num--;
    }
    return num == 0;
}