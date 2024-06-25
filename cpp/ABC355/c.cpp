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
    int N, T;
    cin >> N >> T;
    vi cnt(2*N+2, 0);
    for (int t=0; t<T; t++) {
        int a;
        cin >> a;
        a--;
        int i{a/N}, j{a%N};
        cnt[i] += 1;
        if (cnt[i] == N) {
            cout << t+1;
            return 0;
        }
        cnt[j+N] += 1;
        if (cnt[j+N] == N) {
            cout << t+1;
            return 0;
        }
        if (i == j) {
            cnt[2*N] += 1;
            if (cnt[2*N] == N) {
                cout << t+1;
                return 0;
            }
        }
        if (i+j == N-1) {
            cnt[2*N+1] += 1;
            if (cnt[2*N+1] == N) {
                cout << t+1;
                return 0;
            }
        }
    }
    cout << -1;
}