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
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using vl = vector<long long>;

int main(){
    int N;
    cin >> N;
    vl A;
    for (int i=0; i<N; i++) {
        ll a;
        cin >> a;
        A.emplace_back(a);
    }

    ll ans = 0;
    sort(A.begin(), A.end());
    const ll e8 = 100000000;
    ll count_upe8 = 0;
    for (auto a : A ) {
        auto it = lower_bound(A.begin(), A.end(), e8-a);
        if (it == A.end()) {continue;}
        auto count = distance(it, A.end());
        if (*it <= a) {
            count -= 1;
        }
        count_upe8 += count;
    }

    cout << accumulate(A.begin(), A.end(), 0LL) * (N-1) - e8 * (count_upe8/2);
}