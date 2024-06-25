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

int binary_search(function<bool(int)> f, int l, int r){
    while (r-l > 1){
        int m = l + (r-l)/2;
        if (f(m)){
            r = m;
        } else {
            l = m;
        }
    }
    return r;
}

int N, K;
vi P;

bool f(int x){
    if (x == 0) return false;
    set<int> M{}, m{};
    for (int i=0; i<x; ++i){
        M.insert(-P[i]);
        m.insert(P[i]);
    }
    if (-*M.lower_bound(-N) - *m.lower_bound(0) == K-1) return true;
    for (int i=x; i<N; ++i){
        M.insert(-P[i]);
        m.insert(P[i]);
        M.erase(-P[i-x]);
        m.erase(P[i-x]);
        if (-*M.lower_bound(-N) - *m.lower_bound(0) == K-1) return true;
    }
    return false;
}

int main(){
    cin >> N >> K;
    vi idxs(N, -1);
    for (int i=0; i<N; ++i){
        int p;
        cin >> p;
        P.push_back(p);
        idxs[p-1] = i+1;
    }

    set<int> M{}, m{};
    for (int p=0; p<K; ++p){
        M.insert(-idxs[p]);
        m.insert(idxs[p]);
    }
    int ans{-*M.lower_bound(-N) - *m.lower_bound(0)};
    for (int i=K; i<N; ++i){
        M.insert(-idxs[i]);
        m.insert(idxs[i]);
        M.erase(-idxs[i-K]);
        m.erase(idxs[i-K]);
        ans = min(ans, -*M.lower_bound(-N) - *m.lower_bound(0));
    }

    cout << ans << endl;
}