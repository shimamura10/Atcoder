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

char switchUpLow(const char& s) {
    if (s - 'a' >= 0) {
        return static_cast<char>(s - 'a' + 'A');
    } else {
        return static_cast<char>(s - 'A' + 'a');
    }
}

int main(){
    // input
    string S;
    cin >> S;
    int N = S.size();

    // 対応した閉じかっこの位置をとる
    vi pos_end(N, N);
    vi pos_begin{};
    for (int i=0; i<N; i++) {
        if (S[i] == '(') {
            pos_begin.emplace_back(i);
        } else if (S[i] == ')') {
            pos_end[pos_begin.back()] = i;
            pos_begin.pop_back();
        }
    }

    // しゃくとり法で前から順に位置を決めていく
    int cnt_bracket{0}, next_pos{0}, dir{1};
    vi warp{};
    string ans = S;
    for (int i=0; i<N; i++) {
        const auto& s = S[i];
        if (s == '(') {
            ans[next_pos] = s;
            cnt_bracket++;
            next_pos += (pos_end[i] - i)*dir - dir;
            dir *= -1;
            warp.emplace_back(pos_end[i] - i);
        }
        else if (s == ')') {
            cnt_bracket--;
            dir *= -1;
            ans[next_pos + warp.back()*dir] = s;
            next_pos += warp.back()*dir + dir;
            warp.pop_back();
        } else {
            if (dir == 1) {
                ans[next_pos] = s;
            } else {
                ans[next_pos] = switchUpLow(s);
            }
            next_pos += dir;
        }
    }

    // output
    for (const auto& a : ans) {
        if (a == '(' || a == ')') {
            continue;
        }
        cout << a;
    }
}