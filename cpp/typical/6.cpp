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

int main(){
    int N, K;
    cin >> N >> K;
    string S;
    cin >> S;
    // 与えられた文字列をunixコードにしたもの
    vi vs;
    for (auto s: S) {
        vs.emplace_back(static_cast<int> (s));
    }
    // 現時点で選択可能な文字
    multiset<int> s;
    for (int i=0; i<N-K; i++) {
        s.emplace(static_cast<int> (S[i]));
    }
    reverse(vs.begin(), vs.end());
    vi ans;
    for (int i=N-K; i<N; i++) {
        // 選択可能な文字がひとつ増える
        s.emplace(static_cast<int> (S[i]));
        // 選択可能な文字のうち最も辞書順で若いものを取得
        auto m = *s.begin();
        ans.emplace_back(m);
        // 選択した文字までをvsとsから削除
        while (true) {
            auto b = vs.back();
            auto it = s.find(b);
            s.erase(it, next(it));
            vs.pop_back();
            if (b == m) {
                break;
            }
        }
    }
    for (auto a : ans) {
        cout << static_cast<char> (a);
    }
}