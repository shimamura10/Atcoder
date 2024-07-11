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
    vl A(N);
    multiset<ll> B;
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }
    for (int i = 0; i < M; i++) {
        ll b;
        cin >> b;
        B.insert(b);
    }

    ll ans = 0;
    sort(A.begin(), A.end());
    for (const auto& a : A) {
        auto it = B.upper_bound(a);
        if (it == B.begin()) {
            continue;
        }
        it--;
        ans += a;
        B.erase(it);
    }
    if (!B.empty()) {
        cout << -1 << endl;
        return 0;
    }
    cout << ans << endl;
}