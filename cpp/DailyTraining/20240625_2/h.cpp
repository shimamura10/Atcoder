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

int N, D;

void dfs(int depth, int p, int rest, vi& tmp , vvi& out) {
    if (depth == D) {
        if (rest > p || rest == 0) return;
        tmp.push_back(rest);
        out.emplace_back(tmp);
        tmp.pop_back();
        return;
    }

    auto M = min(p, rest-1);
    for (int i = 1; i <= min(p, rest); i++) {
        tmp.push_back(i);
        dfs(depth+1, i, rest-i, tmp, out);
        tmp.pop_back();
    }
}

void dfs2(int depth, int p, int rest, vi& tmp , vvi& out) {
    if (rest == 0) return;
    if (depth == D) {
        tmp.push_back(rest);
        out.emplace_back(tmp);
        tmp.pop_back();
        return;
    }

    for (int i = 1; i < rest; i++) {
        tmp.push_back(i);
        dfs2(depth+1, i, rest-i, tmp, out);
        tmp.pop_back();
    }
}

int main(){
    cin >> N >> D;
    vector<float> W;
    for (int i = 0; i < N; i++){
        float w;
        cin >> w;
        W.push_back(w);
    }

    sort(W.begin(), W.end());

    vvi cmb{};
    vi tmp{};
    dfs2(1, N, N, tmp, cmb);

    float ans = std::numeric_limits<float>::max();
    for (const auto& c : cmb) {
        vector<float> sums{};
        int accm{0};
        for (const auto& cc : c) {
            float s{0};
            for (int i = accm; i < accm+cc; i++) {
                s += W[i];
            }
            sums.push_back(s);
            accm += cc;
        }
        
        float tmp{0};
        float ave = accumulate(sums.begin(), sums.end(), 0.0) / sums.size();
        for (const auto& s : sums) {
            tmp += pow(s-ave, 2);
        }
        tmp /= sums.size();
        ans = min(ans, tmp);
    }
    cout << ans << endl;
}