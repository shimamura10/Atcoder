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

int main(){
    ll N;
    cin >> N;
    if (N <= 10) {
        cout << N-1 << endl;
        return 0;
    }
    vector<ll> A{10, 9};
    for (ll i = 1; i < 18; i++) {
        A.push_back(pow(10LL, i)*9LL);
        A.push_back(pow(10LL, i)*9LL);
    }
    for (ll i = 0; i < A.size(); i++) {
        if (N <= A[i]) {
            N--;
            vi ans;
            for (ll j = 0; j < i/2+1; j++) {
                ans.push_back(N%10);
                N /= 10;
            }
            ans.back()++;
            string s;
            for (ll j = ans.size()-1; j >= (i+1)%2; j--) {
                s += to_string(ans[j]);
            }
            for (const auto& a : ans) {
                s += to_string(a);
            }
            cout << s << endl;
            return 0;
        }
        N -= A[i];
    }
    return 0;
}