#include <bits/stdc++.h>
using namespace std;

int main(){
    int N, X;
    cin >> N >> X;
    // vector<vector<pair<int, int>>> foods(3, vector<pair<int, int>>());
    // for (int i=0; i<N; i++) {
    //     int v, a, c;
    //     cin >> v >> a >> c;
    //     foods[v-1].push_back(make_pair(a, c));
    // }

    vector<vector<int>> dp(3, vector<int>(X+1, 0));
    for (int i=0; i<N; i++) {
        int v, a, c;
        cin >> v >> a >> c;
        v--;
        for (int j=X; j>=c; j--) {
            dp[v][j] = max(dp[v][j], dp[v][j-c] + a);
        }
    }

    int ans = 0;
    for (int v=0; v<3; v++) {
        for (int i=0; i<=X; i++) {
            int tmpCost = i;
            int tmpValue = dp[v][i];
            for (int ov=0; ov<3; ov++) {
                if (ov == v) {
                    continue;
                }
                if (dp[ov][X] < tmpValue) {
                    tmpCost += X+1;
                    break;
                }
                for (int j=0; j<=X; j++) {
                    if (dp[ov][j] >= tmpValue) {
                        tmpCost += j;
                        break;
                    }
                }
            }
            if (tmpCost <= X) {
                ans = max(ans, tmpValue);
            }
        }
    }

    cout << ans << endl;
}