#include <bits/stdc++.h>
using namespace std;

const int MX = 1000005;
int dat[MX], pre[MX], nxt[MX];
int unused = 1;

void insert(int addr, int num) {

}

void erase(int addr) {

}

void insert_test() {

}

void erase_test() {

}

void traversal() {
    int cur = nxt[0];
    while(cur != -1) {
        cout << dat[cur] << ' ';
        cur = nxt[cur];
    }
    cout << '\n\n';
}

int main() {

    fill(pre, pre + MX, -1);
    fill(nxt, nxt + MX, -1);
    insert_test()
    erase_test()


    return 0;
}