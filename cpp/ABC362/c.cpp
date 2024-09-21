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
const int MOD = 998244353;

int main(){
    int N;
    cin >> N;
    vector<pair<ll, ll>> v(N);
    ll m{0}, M{0};
    for (int i = 0; i < N; i++) {
        cin >> v[i].first >> v[i].second;
        m += v[i].first;
        M += v[i].second;
    }
    if (m > 0 || M < 0) {
        cout << "No" << endl;
        return 0;
    }

    vector<int> used(N, 0);
    ll tmp = 0;
    for (int i=0; i<N; i++) {
        if (v[i].second < 0) {
            tmp += v[i].second;
            used[i] = v[i].second;
        } else if(v[i].first > 0) {
            tmp += v[i].first;
            used[i] = v[i].first;
        }
    }

    for (int i=0; i<N; i++) {
        if (used[i] != 0 || tmp == 0) {
            continue;
        }
        if (tmp > 0) {
            if (v[i].first + tmp >= 0) {
                used[i] = v[i].first;
                tmp += v[i].first;
            } else {
                used[i] = -tmp;
                tmp = 0;
            }
        } else {
            if (v[i].second + tmp <= 0) {
                used[i] = v[i].second;
                tmp += v[i].second;
            } else {
                used[i] = -tmp;
                tmp = 0;
            }
        }
    }

    for (int i=0; i<N; i++) {
        if (tmp == 0) {
            break;
        }
        if (tmp > 0 && v[i].first - used[i] < 0) {
            auto diff = v[i].first - used[i];
            if (diff + tmp >= 0) {
                used[i] = v[i].first;
                tmp += diff;
            } else {
                used[i] = -tmp;
                tmp = 0;
            }
        } else if (tmp < 0 && v[i].second > used[i]) {
            auto diff = v[i].second - used[i];
            if (diff + tmp <= 0) {
                used[i] = v[i].second;
                tmp += diff;
            } else {
                used[i] = -tmp;
                tmp = 0;
            }
        }
    }

    cout << "Yes" << endl;
    for (const auto& u : used) {
        cout << u << " ";
    }
}