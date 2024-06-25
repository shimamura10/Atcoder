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
const ll MOD = 1000000007;

int main(){
    int N;
    cin >> N;
    string S;
    cin >> S;
    vi numS{};
    string target = "atcoder";
    for (auto s: S) {
        for (int i=0; i<7; i++) {
            if (s == target[i]) {
                numS.emplace_back(i);
            }
        }
    }

    vl cntNum(7, 0LL);
    for (auto num: numS) {
        if (num == 0) {
            cntNum[0]++;
        } else {
            cntNum[num] = (cntNum[num] + cntNum[num-1]) % MOD;
        }
    }

    cout << cntNum[6] << endl;
}