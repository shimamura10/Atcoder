#include<bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i=0; i<N; i++) {
        cin >> A[i];
    }
    unordered_map<int, int> lastPos;
    int ans = A.size() + 1;
    for (int i=0; i<A.size(); i++) {
        if (lastPos.find(A[i]) != lastPos.end()) {
            ans = min(ans, i - lastPos[A[i]] + 1);
        }
        lastPos[A[i]] = i;
    }
    cout << (ans == A.size() + 1 ? -1 : ans) << endl;
}