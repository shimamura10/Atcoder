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
    int N;
    cin >> N;
    vl H(N);
    for(int i = 0; i < N; ++i){
        cin >> H[i];
    }
    ll ans = 0;
    vector<pair<ll, ll>> walls{{1000000000, -1}};
    for (ll i=0; i<N; ++i){
        ll tmp = 0;
        while (walls.back().first < H[i]){
            auto wall = walls.back();
            walls.pop_back();
            tmp += wall.first * (wall.second - walls.back().second);
        }
        ans += (i-walls.back().second)*H[i] - tmp;
        walls.emplace_back(H[i], i);
        cout << ans + 1 << " ";
    }
}