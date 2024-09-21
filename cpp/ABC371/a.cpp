#include<bits/stdc++.h>
using namespace std;

void solve(char ab, char ac, char bc) {
    vector<int> v = {0, 1, 2};
    do {
        if (ab == '<') {
            if (v[0] > v[1]) continue;
        } else if (ab == '>') {
            if (v[0] < v[1]) continue;
        } 
        if (ac == '<') {
            if (v[0] > v[2]) continue;
        } else if (ac == '>') {
            if (v[0] < v[2]) continue;
        }
        if (bc == '<') {
            if (v[1] > v[2]) continue;
        } else if (bc == '>') {
            if (v[1] < v[2]) continue;
        } 
        break;
    } while (next_permutation(v.begin(), v.end()));
    char ans[3] = {'A', 'B', 'C'};
    for (int i=0; i<3; i++) {
        if (v[i] == 1) {
            cout << ans[i];
        }
    }
}

int main() {
    char ab, ac, bc;
    cin >> ab >> ac >> bc;
    solve(ab, ac, bc);
    return 0;
}