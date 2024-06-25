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
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using vl = vector<long long>;

int count_twos(ll n)
{
    int ret{0};
    while (n%2 == 0 && n > 1)
    {
        ret++;
        n /= 2;
    }
    return ret;
}

int main(){
    ll L, R;
    cin >> L >> R;
    ll l{L};
    vector<pair<ll, ll>> ans{};
    if (l == 0) {
        ll r{1};
        while (r*2 <= R)
        {
            r *= 2;
        }
        ans.emplace_back(l, r);
        l = r;
    }
    while (l<R)
    {
        auto num_tows = count_twos(l);
        ll d{1LL<<num_tows};
        while (l + d > R)
        {
            d /= 2;
        }
        ans.emplace_back(l, l+d);
        l += d;
    }
    cout << ans.size() << endl;
    for (auto a: ans) {
        cout << a.first << " " << a.second << endl;
    }
}