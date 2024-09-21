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
using namespace std;
using ll = long long;

int main(){
    int N;
    cin >> N;
    unordered_map<ll, ll> delicious_values;
    for (int i=0; i<N; i++) {
        ll a, c;
        cin >> a >> c;
        // delicious_values.try_emplace(c, a);
        if (delicious_values.count(c) == 0) {
            delicious_values.emplace(c, a);
        } else {
            delicious_values[c] = min(delicious_values[c], a);
        }
    }

    ll ans{0};
    for (const auto& [key, value] : delicious_values ) {
        ans = max(ans, value);
    }
    cout << ans;
}