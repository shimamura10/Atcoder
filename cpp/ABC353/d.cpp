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
#include <string>
#include <complex>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using vl = vector<long long>;
const ll mod = 998244353;

int main(){
    int N;
    cin >> N;
    vector<string> A;
    for (int i=0; i<N; i++) {
        string a;
        cin >> a;
        A.emplace_back(a);
    }

    reverse(A.begin(), A.end());
    ll len_sum = 0;
    ll ans = 0;
    ll ind = 0;
    for (auto a : A) {
        auto la = stoll(a);
        ans += la*len_sum;
        ans %= mod;
        ans += la*(N - ++ind);
        ans %= mod;
        len_sum += pow(10, a.length());
        len_sum %= mod;
    }
    cout << ans;
}