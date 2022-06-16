#include <string>
#include <vector>

using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {
    vector<string> answer;
    for(int i = 0; i < n; i++) {
        int first = arr1[i];
        int second = arr2[i];
        int newMap = first | second;
        string s = "";
        for(int j = 0; j < n; j++) {
            if(newMap % 2 == 0) {
                s = " " + s;
            } else {
                s = "#" + s;
            }
            newMap /= 2;
        }
        answer.push_back(s);
    }
    return answer;
}