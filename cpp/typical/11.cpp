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
    vector<vector<ll>> jobs(N, vector<ll>(3));
    vector<ll> dp(5001, 0);
    for (int i=0; i<N; i++) {
        int d, c;
        ll s;
        cin >> d >> c >> s;
        jobs[i] = {d, c, s};
    }

    sort(jobs.begin(), jobs.end(), [](const vector<ll>& a, const vector<ll>& b){
        return a[0] < b[0];
    });

    for (const auto& job: jobs) {
        for (int j=job[0]; j>=job[1]; j--) {
            dp[j] = max(dp[j], dp[j-job[1]]+job[2]);
        }
    }

    cout << *max_element(dp.begin(), dp.end()) << endl;
}