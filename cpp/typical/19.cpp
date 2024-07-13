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

int N;
vi A{};
unordered_map<int, int> rets{};
int dfs(int l, int r)
{
    if (r-l <= 0) return 0;
    if (rets.find(l*2*N + r) != rets.end()) return rets[l*2*N + r];
    if (r-l == 1) return rets[l*2*N + r] = abs(A[l] - A[r]);
    int ret = INT_MAX;
    for (int i=l+1; i<r; i+=2)
    {
        // int tmp = dfs(l, i);
        // for (int j=i+1; j<r; j+=2)
        // {
        //     int tmp2 = dfs(i+1, j-1) + dfs(j, r);
        //     ret = min(ret, tmp + tmp2);
        // }
        ret = min(ret, dfs(l, i) + dfs(i+1, r));
    }
    ret = min(ret, dfs(l+1, r-1) + abs(A[l] - A[r]));
    return rets[l*2*N + r] = ret;
}

int main(){
    cin >> N;
    A.resize(2*N);
    for (int i = 0; i < 2*N; i++)
    {
        cin >> A[i];
    }
    cout << dfs(0, 2*N-1) << endl;
    return 0;
}