#include<bits/stdc++.h>
using namespace std;

int main() {
    int N, W;
    cin >> N >> W;
    vector<vector<pair<int, int>>> A(W);
    for (int i=0; i<N; i++) {
        int x, y;
        cin >> x >> y;
        x--; y--;
        A[x].emplace_back(y, i);
    }
    sort(A.begin(), A.end(), [](const vector<pair<int, int>>& a, const vector<pair<int, int>>& b) {
        return a.size() > b.size();
    });
    for (int i=0; i<W; i++) {
        sort(A[i].begin(), A[i].end());
    }
    vector<int> ans(N, 1000000001);
    // int acc = 0;
    int mimLen = N;
    for (int i=0; i<W; i++) {
        mimLen = min(mimLen, (int)A[i].size());
    }
    for (int i=0; i<mimLen; i++) {
        if (A[0].size() <= i) {
            break;
        }
        int tmp = A[0][i].first;
        for (int j=0; j<W; j++) {
            if (A[j].size() <= i) {
                break;
            }
            tmp = max(tmp, A[j][i].first);
        }
        for (int j=0; j<W; j++) {
            if (A[j].size() <= i) {
                break;
            }
            ans[A[j][i].second] = tmp;
        }
    }

    int Q;
    cin >> Q;
    for (int i=0; i<Q; i++) {
        int t, a;
        cin >> t >> a;
        t--; a--;
        if (ans[a] > t) {
            cout << "Yes" << endl;
        } else {
            cout << "No" << endl;
        }
    }
}