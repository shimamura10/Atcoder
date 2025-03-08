#include<bits/stdc++.h>
using namespace std;

int main() {
    unordered_map<int, int> m;
    for (int i=0; i<4; i++) {
        int a;
        cin >> a;
        m[a]++;
    }
    int ans = 0;
    for (auto [key, value] : m) {
        ans += value/2;
    }
    cout << ans << endl;
}