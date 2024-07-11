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
    int N, D, P;
    cin >> N >> D >> P;
    vl F(N);
    for (int i = 0; i < N; ++i){
        cin >> F[i];
    }
    sort(F.begin(), F.end(), greater<ll>());

    auto ans = accumulate(F.begin(), F.end(), 0LL);
    auto tmp = ans;
    for (int i = 0; i < N/D+1; i++) {
        tmp -= accumulate(F.begin()+i*D, F.begin()+min(N, (i+1)*D), 0LL);
        tmp += P;
        ans = min(ans, tmp);
    }

    cout << ans << endl;
}