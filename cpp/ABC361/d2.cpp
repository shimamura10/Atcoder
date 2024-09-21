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
    string S, T;
    cin >> N >> S >> T;
    S += "..";
    T += "..";
    unordered_set<string> visited{S};
    queue<pair<int, string>> que{};
    que.emplace(0, S);
    while (!que.empty()) {
        auto [c, s] = que.front();
        que.pop();
        if (s == T) {
            cout << c << endl;
            return 0;
        }
        int idx;
        for (int i = 0; i < N+2; i++) {
            if (s[i] == '.') {
                idx = i;
                break;
            }
        }
        for (int i = 0; i < N+1; i++) {
            if (s[i] == '.' || s[i+1] == '.') {
                continue;
            }
            string ns = s;
            swap(ns[i], ns[idx]);
            swap(ns[i+1], ns[idx+1]);
            if (visited.count(ns) == 0) {
                visited.insert(ns);
                que.emplace(c+1, ns);
            }
        }
    }
    cout << -1 << endl;
}