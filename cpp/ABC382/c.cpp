#include<bits/stdc++.h>
using namespace std;

void solve(int N, int M, vector<int>& A, vector<int>& B) {
    vector<pair<int, int>> oisisa;
    for (int i=0; i<M; i++) {
        oisisa.emplace_back(B[i], i);
    }
    sort(oisisa.begin(), oisisa.end());
    vector<int> ans(M, -1);
    for (int i=0; i<N; i++) {
        auto it = lower_bound(oisisa.begin(), oisisa.end(), 
        make_pair(A[i], 0),
        [] (const pair<int, int>& a, const pair<int, int>& b) {
            return a.first < b.first;
        });
        while (it != oisisa.end() && ans[it->second] == -1) {
            ans[it->second] = i+1;
            it++;
        }
    }
    for (const auto& a : ans) {
        cout << a << endl;
    }
}

int main() {
    int N, M;
    cin >> N >> M;
    vector<int> A(N);
    for (int i=0; i<N; i++) {
        cin >> A[i];
    }
    vector<int> B(M);
    for (int i=0; i<M; i++) {
        cin >> B[i];
    }

    solve(N, M, A, B);
    return 0;
}