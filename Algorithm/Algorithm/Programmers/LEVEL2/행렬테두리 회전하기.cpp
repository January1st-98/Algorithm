#include <bits/stdc++.h>

using namespace std;

vector<int> solution(int rows, int columns, vector<vector<int>> queries) {
    vector<int> answer;
    int board[102][102];
    int num = 1;
    
    for(int i = 0; i < rows + 2; i++) {
        fill(board[i], board[i] + columns + 1, 0);
    }
    
    for(int i = 1; i <= rows; i++) {
        for(int j = 1; j <= columns; j++) {
            board[i][j] = num;
            num++;
        }
    }
    for(auto q: queries) {
        int x1 = q[0], y1 = q[1], x2 = q[2], y2 = q[3];
        vector<int> v;
        int num_count = 0;
        int blocks = ((x2-x1)+(y2-y1)) * 2;
        int x = x1, y = y1;
        while(num_count < blocks) {
            v.push_back(board[x][y]);
            if(x == x1 && y != y2) {
                y = y + 1;
            }
            else if(y == y2 && x != x2) {
                x = x + 1;
            }
            else if(x == x2 && y != y1) {
                y = y - 1;
            }
            else if(y == y1 && x != x1) {
                x = x - 1;
            }
            num_count++;
        }
        rotate(v.begin(), v.end()-1, v.end());
        cout << * min_element(v.begin(), v.end()) << '\n';
        answer.push_back(*min_element(v.begin(), v.end()));
        num_count = 0;
        x = x1; y = y1;
        while(num_count < blocks) {
            board[x][y] = v[num_count];
            if(x == x1 && y != y2) {
                y = y + 1;
            }
            else if(y == y2 && x != x2) {
                x = x + 1;
            }
            else if(x == x2 && y != y1) {
                y = y - 1;
            }
            else if(y == y1 && x != x1) {
                x = x - 1;
            }
            num_count++;
        }
        
    }
    return answer;
}