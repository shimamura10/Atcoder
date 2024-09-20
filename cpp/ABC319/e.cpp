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

int N;
ll X, Y;
vector<pair<int, ll>> bus{};

ll query(ll start) {
    start += X;
    for (const auto& [p, t] : bus) {
        if (start % p == 0) {
            start += t;
        } else {
            start += p - start % p + t;
        }
    }
    return start + Y;
}

int main(){
    cin >> N >> X >> Y;
    for (int i = 0; i < N-1; i++) {
        ll A, B;
        cin >> A >> B;
        bus.emplace_back(A, B);
    }

    vl dif{};
    for (int i = 0; i < 840; i++) {
        dif.push_back(query(i) - i);
    }

    int Q;
    cin >> Q;
    for (int i = 0; i < Q; i++) {
        ll q;
        cin >> q;
        cout << q + dif[q%840] << endl;
    }

    // while (true) {
    //     ll q;
    //     cin >> q;
    //     cout << query(q) - q << endl;
    // }
    // int c = 29;
    // for (int i = 0; i < c; i++) {
    //     auto q1 = query(i) - i;
    //     auto q2 = query(c+i) - (c+i);
    //     if (q1 != q2) {
    //         cout << "NO" << endl;
    //         cout << "i: " << i << endl;
    //         // return 0;
    //     }
    // }
}