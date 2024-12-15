#include<bits/stdc++.h>
using namespace std;

int main() {
    long long N, K;
    cin >> N >> K;
    vector<int> v(N);
    for (int i = 0; i < N; i++) {
        cin >> v[i];
    }

    for (int i=0; i<K; i++) {
        vector<int> nv(N, 0);
        for (int j=0; j<N; j++) {
            nv[j] = v[v[j]-1];
        }
        for (const auto& e : nv) {
            cout << e << " ";
        }
        cout << endl;
        v = nv;
    }
}