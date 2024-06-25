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

// aのi番目を末尾にもつ最長増加部分列の長さを求める。
vi LIS(const vi& A) 
{
    vi ret{};
    vi dp(A.size(), INT_MAX);
    for (const auto& a: A) {
        auto idx = lower_bound(dp.begin(), dp.end(), a) - dp.begin();
        dp[idx] = a;
        ret.emplace_back(idx+1);
    }
    return ret;
}

int main(){
    int T;
    cin >> T;
    for (int t=0; t<T; t++) {
        int N;
        cin >> N;
        vi A;
        for (int i=0; i<N; i++) {
            int a;
            cin >> a;
            A.emplace_back(a);
        }
        auto lis = LIS(A);
        // reverse(lis.begin(), lis.end());
        auto M = *max_element(lis.begin(), lis.end());
        // maxNum[i] = a: LISがi+1となる数のうち最大値はa
        vi maxNum(M, 0);
        vi ans{};
        for (int i=N-1; i>=0; i--) {
            int& tmp_lis = lis[i];
            if (tmp_lis == M) {
                maxNum[tmp_lis-1] = max(maxNum[tmp_lis-1], A[i]);
                ans.emplace_back(i+1);
            } else {
                if (A[i] < maxNum[tmp_lis]) {
                    maxNum[tmp_lis-1] = max(maxNum[tmp_lis-1], A[i]);
                    ans.emplace_back(i+1);
                }
            }
        }

        reverse(ans.begin(), ans.end());
        cout << ans.size() << "\n";
        for (auto& a : ans) {
            cout << a << " ";
        }
        cout << "\n";
    }
}