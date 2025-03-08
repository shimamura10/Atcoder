#include<bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    unordered_map<int, int> m;
    for (int i=0; i<N; i++) {
        int a;
        cin >> a;
        if (m.find(a) == m.end()) {
            m[a] = i + 1;
            cout << -1 << " ";
        } else {
            cout << m[a] << " ";
            m[a] = i + 1;
        }
    }
}