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

int N, K;
ll L;
vl A;

int binary_search(function<bool(int)> f, int l, int r){
    while (r-l > 1){
        int m = l + (r-l)/2;
        if (f(m)){
            r = m;
        } else {
            l = m;
        }
    }
    return l;
}

bool check(int x){
    int cnt = 0;
    ll prev = 0;
    for (int i=0; i<N; ++i){
        if (A[i] - prev >= x){
            prev = A[i];
            cnt++;
        } 
    }
    if (A[N] - prev < x) cnt--;
    return !(cnt >= K);
}

int main(){
    cin >> N >> L >> K;
    A.resize(N);
    for (int i=0; i<N; ++i) {
        cin >> A[i];
    }
    A.emplace_back(L);

    cout << binary_search(check, 0, L) << endl;
}