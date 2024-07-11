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

// 受け取ったviの要素のうち、2以上のものが唯一であればその要素のインデックスを返す
// そうでなければ-1を返す
int check(const vi& v){
    int exist = -1;
    for (int i = 0; i < v.size(); ++i){
        if (v[i] > 0){
            if (exist == -1){
                exist = i;
            } else {
                return -1;
            }
        }
    }
    if (exist != -1 && v[exist] > 1){
        return exist;
    }
    return -1;
}

int main(){
    int H, W;
    cin >> H >> W;
    vvi A(H+W, vi(26, 0));
    for (int i = 0; i < H; ++i){
        for (int j = 0; j < W; ++j){
            char c;
            cin >> c;
            A[i][c-'a']++;
            A[H+j][c-'a']++;
        }
    }

    vector<bool> erased(H+W, false);
    vector<pair<int, int>> stack{};
    for (int i = 0; i < H+W; ++i){
        auto exist = check(A[i]);
        if (exist != -1){
            stack.emplace_back(i, exist);
            erased[i] = true;
        }
    }

    vector<pair<int, int>> nextStack{};
    while (!stack.empty()){
        auto [tmp, col] = stack.back();
        stack.pop_back();
        A[tmp][col] = 0;
        if (tmp < H) {
            for (int i = H; i < H+W; ++i){
                if (erased[i]){
                    continue;
                }
                A[i][col]--;
                auto exist = check(A[i]);
                if (exist != -1){
                    nextStack.emplace_back(i, exist);
                    erased[i] = true;
                }
            }
        } else {
            for (int i = 0; i < H; ++i){
                if (erased[i]){
                    continue;
                }
                A[i][col]--;
                auto exist = check(A[i]);
                if (exist != -1){
                    nextStack.emplace_back(i, exist);
                    erased[i] = true;
                }
            }
        }
        if (stack.empty()){
            stack = nextStack;
            nextStack.clear();
        }
    }

    int ans{0};
    for (int i = 0; i < H; i++) {
        for (const auto& a : A[i]) {
            ans += max(a, 0);
        }
    }

    cout << ans << endl;
}