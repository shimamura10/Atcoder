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

template<class T> size_t HashCombine(const size_t seed,const T &v){
    return seed^(std::hash<T>()(v)+0x9e3779b9+(seed<<6)+(seed>>2));
}
/* pair用 */
template<class T,class S> struct std::hash<std::pair<T,S>>{
    size_t operator()(const std::pair<T,S> &keyval) const noexcept {
        return HashCombine(std::hash<T>()(keyval.first), keyval.second);
    }
};
/* vector用 */
template<class T> struct std::hash<std::vector<T>>{
    size_t operator()(const std::vector<T> &keyval) const noexcept {
        size_t s=0;
        for (auto&& v: keyval) s=HashCombine(s,v);
        return s;
    }
};

struct InputCreator {
    std::default_random_engine _engine;
    InputCreator() {
        std::random_device seed_gen;
        _engine = std::default_random_engine(seed_gen());
    }

    // [a, b]の整数をランダムに生成
    int randint(int a, int b) {
        std::uniform_int_distribution<int> dist(a, b);
        return dist(_engine);
    }

    // 長さNで、[a, b]の要素を持つvectorを生成
    vi randints(int N, int a, int b) {
        vi res(N);
        for (int i=0; i<N; i++) {
            res[i] = randint(a, b);
        }
        return res;
    }
};

int solve1(const int N, const string S, const string T) {
    pair<int, int> s{0, N}, t{0, N};
    for (int i = 0; i < N; i++){
        if (S[i] == 'B') {
            s.first += 1<<i;
        }
        if (T[i] == 'B') {
            t.first += 1<<i;
        }
    }
    unordered_set<pair<int, int>> visited{s};
    queue<pair<int, pair<int, int>>> que{};
    que.emplace(0, s);
    while (!que.empty()){
        auto [c, ps] = que.front(); 
        que.pop();
        if (ps == t) {
            return c;
        }
        auto s{ps.first}, idx{ps.second};
        for (int i = 0; i <= N; i++) {
            if (i >= idx-1 && i <= idx+1) continue;
            auto ns{s};
            int ni = (s>>i) & 1;
            int ni1 = (s>>(i+1)) & 1;
            // 二進数nsのidx, idx+1桁目をi, i+1桁目に変更する
            ns |= ni << idx | ni1 << (idx+1);
            // 二進数nsのi, i+1桁目を0にする
            ns &= ~(1<<i | 1<<(i+1));
            // if (ns == t.first && i == t.second){
            //     return c+1;
            // }
            pair<int, int> pns{ns, i};
            if (visited.find(pns) == visited.end()){
                visited.insert(pns);
                que.emplace(c+1, pns);
            }
        }
    }
    return -1;
}

int solve2(int N, string S, string T) {
    S += "..";
    T += "..";
    unordered_set<string> visited{S};
    queue<pair<int, string>> que{};
    que.emplace(0, S);
    while (!que.empty()) {
        auto [c, s] = que.front();
        que.pop();
        if (s == T) {
            return c;
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
    return -1;
}

int main(){
    for (int _=0; _<100; _++) {
        InputCreator ic{};
        int N = ic.randint(1, 10);
        auto bools = ic.randints(N, 0, 1);
        string S = "";
        for (int i=0; i<N; i++) {
            S += bools[i] ? "B" : "W";
        }
        string T = S;
        random_shuffle(T.begin(), T.end());

        int res1 = solve1(N, S, T);
        int res2 = solve2(N, S, T);
        if (res1 != res2) {
            cout << "Mismatched! N: " << N << ", S: " << S << ", T: " << T << endl;
            cout << "Expected: " << res1 << ", Got: " << res2 << endl;
        }
    }
}