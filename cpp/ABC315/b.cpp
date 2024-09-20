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
    int M;
    cin >> M;
    vi D(M);
    for (int i = 0; i < M; ++i){
        cin >> D[i];
    }
    auto mid = accumulate(D.begin(), D.end(), 1) / 2;
    int cnt = 0;
    for (int i = 0; i < M; ++i) {
        if (cnt + D[i] >= mid){
            cout << i + 1 << " " << mid - cnt << endl;
            return 0;
        }
        cnt += D[i];
    }
}