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

    int ans2{1000};
    int m2, M2, num;
    for (int i=1; i<=N-K+1; i++) {
        int m{1000};
        int M{-1};
        for (int j=0; j<K; j++) {
            int ind{0};
            for (auto p : P) {
                if (p == i+j) {
                    break;
                }
                ind++;
            }
            m = min(m, ind);
            M = max(M, ind);
        }
        auto tmp = M-m;
        if (ans2 > tmp) {
            ans2 = tmp;
            m2 = m;
            M2 = M;
            num = i;
        }
        // ans2 = min(ans2, M-m);
    }
    cout << ans2;
}