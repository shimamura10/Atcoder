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
    int N;
    cin >> N;
    vvi A(N);
    for (int i = 0; i < N; ++i) {
        int a;
        cin >> a;
        A[a-1].emplace_back(i);
    }

    ll ans{0};
    for (const auto& va : A) {
        if (va.size() <= 1) continue;
        ll cntj = 0;
        int prea = va[0];
        for (int j = 1; j < va.size(); ++j){
            ans += (cntj+va[j]-prea-1)*j;
            cntj += 
        }
    }
}