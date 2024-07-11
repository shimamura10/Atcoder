#include <iostream>
#include <algorithm>
#include <vector>
#include <functional>
#include <unordered_map>
#include <memory>
#include <queue>
#include <unordered_set>
#include <limits>
#include <tuple>
#include <numeric>
#include <set>
#include <random>
#include <string>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using vl = vector<long long>;
const ll MOD = 998244353;

int main(){
    int N, M;
    cin >> N >> M;
    vi A(N);
    for (int i = 0; i < N; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < M; j++) {
            if (s[j] == 'o') {
                A[i] |= 1 << j;
            }
        }
    }
    int ans = N;
    for (int i = 0; i < (1 << N); i++) {
        int tmp = 0;
        int cnt = 0;
        for (int j = 0; j < N; j++) {
            if (i >> j & 1) {
                tmp |= A[j];
                cnt++;
            }
        }
        if ((1 << M) - 1 == tmp) {
            ans = min(ans, cnt);
        }
    }
    cout << ans << endl;
}   