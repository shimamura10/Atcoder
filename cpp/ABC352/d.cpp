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
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using vl = vector<long long>;

int main(){
    int N, K;
    cin >> N >> K;
    vi P;
    unordered_map<int, int> pos;
    for (int i=0; i<N; i++) {
        int p;
        cin >> p;
        P.emplace_back(p);
        pos[p] = i;
    }

    set<int> s;
    for (int i=1; i<K; i++) {
        s.insert(pos[i]);
    }

    int ans{K};
    for (int i=K; i<=N; i++) {
        s.insert(pos[i]);
        ans = min(ans, *s.rbegin() - *s.begin());
        s.erase(pos[i-K+1]);
    }

    cout << ans;
}