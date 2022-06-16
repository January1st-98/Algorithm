#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;
    int prev = -1;
    for(int i = 0; i < arr.size(); i++) {
        if(arr[i] == prev) continue;
        else {
            answer.push_back(arr[i]);
            prev = arr[i];
        }
    }
    return answer;
}