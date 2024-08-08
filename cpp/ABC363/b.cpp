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
    int N, T, P;
    cin >> N >> T >> P;
    vi L(N);
    for(int i = 0; i < N; ++i){
        cin >> L[i];
    }
    sort(L.begin(), L.end());
    auto ans = T - L[N-P];
    cout << max(ans, 0) << endl;
}