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


vvi permutate(int N) {
    vvi res;
    vi v(N);
    iota(v.begin(), v.end(), 0);
    do {
        res.push_back(v);
    } while (next_permutation(v.begin(), v.end()));
    return res;
}


int main(){
    int N, M;
    vector<vector<int>> G(N);
    cin >> N >> M;
    G.resize(N, vector<int>(N, -1));
    for (int i = 0; i < M; ++i){
        int a, b, c;
        cin >> a >> b >> c;
        --a; --b;
        G[a][b] = c;
        G[b][a] = c;
    }

    auto perms = permutate(N);
    int ans = 0;
    for (auto perm : perms){
        int sum = 0;
        for (int i = 0; i < N-1; ++i){
            if (G[perm[i]][perm[i+1]] == -1){
                break;
            }
            sum += G[perm[i]][perm[i+1]];
        }
        ans = max(ans, sum);
    }

    cout << ans << endl;

}