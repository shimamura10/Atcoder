#include<bits/stdc++.h>
using namespace std;

int main() {
    int N, D;
    cin >> N >> D;
    string S;
    cin >> S;
    int ans = D;
    for (const auto& c : S) {
        if (c == '.') {
            ans++;
        }
    }
    cout << ans << endl;
    return 0;
}