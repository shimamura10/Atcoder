#include<bits/stdc++.h>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    vector<int> A(M);
    for (int i = 0; i < M; i++) {
        cin >> A[i];
    }
    sort(A.begin(), A.end());
    int tmp = 0;
    vector<int> ans{};
    for (int i=1; i<N+1; i++) {
        if (A[tmp] == i) {
            tmp++;
        } else {
            ans.push_back(i);
        }
    }
    cout << ans.size() << endl;
    for (const auto& a : ans) {
        cout << a << " ";
    }
    cout << endl;
    return 0;
}