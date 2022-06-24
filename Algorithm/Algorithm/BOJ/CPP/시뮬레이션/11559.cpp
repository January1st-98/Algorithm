#include <bits/stdc++.h>
using namespace std;

string board[13];
bool vis[13][7];
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

int main() {
    cout.sync_with_stdio(0);
    cin.tie(0);

    for(int i = 0; i < 12; i++) {
        cin >> board[i];
    }
    int ans = 0;
    while(true){
        bool is_chain = false;
        for(int i = 0; i < 12; i++) {
            fill(vis[i], vis[i] + 6, false);
        }
        queue<pair<int, int>> Q;
        for(int i = 0; i < 12; i++) {
            for(int j = 0; j < 6; j++) {
                if(board[i][j] == '.' || vis[i][j]) continue;
                int counted = 1;
                Q.push({i, j});
                vis[i][j] = true;
                vector<pair<int, int>> coor;
                coor.push_back({i, j});
                while(!Q.empty()){
                    auto cur = Q.front(); Q.pop();
                    char cur_color = board[cur.first][cur.second];
                    for(int dir = 0; dir < 4; dir++) {
                        int nx = cur.first + dx[dir];
                        int ny = cur.second + dy[dir];
                        if(nx < 0 || nx >= 12 || ny < 0 || ny >= 6) continue;
                        if(vis[nx][ny]) continue;
                        if(board[nx][ny] != cur_color) continue;
                        vis[nx][ny] = true;
                        Q.push({nx, ny});
                        coor.push_back({nx, ny});
                        counted++;
                    }
                }
                if(counted >= 4) {
                    is_chain = true;
                    for(auto c: coor) {
                        board[c.first][c.second] = '.';
                    }
                }
            }
        }

        //블럭을 아래로 내리는 작업
        if(is_chain) {
            ans++;
            for(int i = 0; i < 6; i++) {
                for(int j = 10; j >= 0; j--) {
                    int tmp = j;
                    while(tmp < 11 && board[tmp + 1][i] == '.') {
                        swap(board[tmp][i], board[tmp+1][i]);
                        tmp++;
                    }
                }
            }
        }


        if(!is_chain) break;
    }
    cout << ans;

    return 0;
}

