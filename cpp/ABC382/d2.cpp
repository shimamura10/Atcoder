#include<bits/stdc++.h>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    vector<vector<int>> ans;
    int sum = M - 10*(N-1) - 1;
    auto dfs = [&] (auto&& self, vector<int>& A) -> void {
        int amari = sum - accumulate(A.begin(), A.end(), 0);
        if (A.size() == N) {
            A.push_back(amari);
            ans.push_back(A);
            A.pop_back();
            return;
        }
        for (int i=0; i<=amari; i++) {
            A.push_back(i);
            self(self, A);
            A.pop_back();
        }
    };
    vector<int> A{};
    dfs(dfs, A);
    cout << ans.size() << endl;
    for (auto& a : ans) {
        int tmp = 1 + a[0];
        for (int i=0; i<N; i++) {
            cout << tmp << " ";
            tmp += 10 + a[i+1];
        }
        cout << endl;
    }
}