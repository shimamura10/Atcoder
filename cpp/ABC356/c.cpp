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
    int N, M, K;
    cin >> N >> M >> K;
    vvi A{};
    vector<bool> R{};
    for (int i=0; i<M; i++) {
        int c;
        cin >> c;
        vi tmp{};
        for (int j=0; j<c; j++) {
            int a;
            cin >> a;
            tmp.emplace_back(a-1);
        }
        A.emplace_back(tmp);
        char r;
        cin >> r;
        if (r == 'o') {
            R.emplace_back(true);
        } else {
            R.emplace_back(false);
        }
    }

    int ans{0};
    for (int bit=0; bit < 1<<N; bit++) {
        bool ok{true};
        for (int i=0; i<M; i++) {
            int cnt{0};
            for (const auto& a: A[i]) {
                if (bit>>a & 1) {
                    cnt++;
                }
            }
            
            if (R[i]) {
                if (cnt < K) {
                    ok = false;
                    break;
                }
            } else {
                if (cnt >= K) {
                    ok = false;
                    break;
                }
            }
        }
        if (ok) {
            ans++;
        }
    }

    cout << ans;
}