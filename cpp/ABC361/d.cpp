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

int main(){
    int N;
    string S, T;
    cin >> N >> S >> T;
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
            cout << c << endl;
            return 0;
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
            pair<int, int> pns{ns, i};
            if (visited.find(pns) == visited.end()){
                visited.insert(pns);
                que.emplace(c+1, pns);
            }
        }
    }
    cout << -1 << endl;
}