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
#include <numbers>
#include <iomanip>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using vl = vector<long long>;
const ll MOD = 998244353;

bool check(int i, const vi& C, const vector<bool>& used) {
    int h = i / 3;
    int w = i % 3;
    bool flag = false;
    // check row
    for (int j = 0; j < 3; j++) {
        if (!used[h*3 + j]) continue;
        if (C[i] == C[h*3+j]) {
            flag = true;
        } else {
            flag = false;
            break;
        }
    }
    if (flag) return true;

    // check column
    for (int j = 0; j < 3; j++) {
        if (!used[j*3+w]) continue;
        if (C[i] == C[j*3+w]) {
            flag = true;
        } else {
            flag = false;
            break;
        }
    }
    if (flag) return true;

    // check diagonal
    if (h == w) {
        for (int j = 0; j < 3; j++) {
            if (!used[j*3+j]) continue;
            if (C[i] == C[j*3+j]) {
                flag = true;
            } else {
                flag = false;
                break;
            }
        }
        if (flag) return true;
    }

    if (h + w == 2) {
        for (int j = 0; j < 3; j++) {
            if (!used[j*3+2-j]) continue;
            if (C[i] == C[j*3+2-j]) {
                flag = true;
            } else {
                flag = false;
                break;
            }
        }
        if (flag) return true;
    }

    return false;
}

int main(){
    vi C(9);
    for (int i = 0; i < 9; i++) cin >> C[i];

    vi perm{0, 1, 2, 3, 4, 5, 6, 7, 8};
    int cnt = 0;
    do {
        vector<bool> used(9, false);
        bool flag = true;
        for (const auto& v : perm) {
            if (check(v, C, used)) {
                flag = false;
                break;
            }
            used[v] = true;
        }
        if (flag) {
            cnt++;
        }
    } while (next_permutation(perm.begin(), perm.end()));

    int fact9 = 1;
    for (int i = 1; i <= 9; i++) {
        fact9 *= i;
    }
    cout << fixed << setprecision(10) << static_cast<double>(cnt) / static_cast<double>(fact9) << endl;
}