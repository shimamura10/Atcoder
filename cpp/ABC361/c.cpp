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
    int N, K;
    cin >> N >> K;
    vi A(N);
    for (int i=0; i<N; i++){
        cin >> A[i];
    }
    sort(A.begin(), A.end());
    int ans = INT_MAX;
    auto d = N - K;
    for (int i=0; i<N-d+1; i++){
        ans = min(ans, A[i+d-1]-A[i]);
    }
    cout << ans << endl;
}