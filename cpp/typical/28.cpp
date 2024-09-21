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
    int N;
    cin >> N;
    vvi A(1001, vi(1001));
    for (int i = 0; i < N; i++){
        int lx, ly, rx, ry;
        cin >> lx >> ly >> rx >> ry;
        A[lx][ly]++;
        A[rx][ry]++;
        A[lx][ry]--;
        A[rx][ly]--;
    }
    for (int i = 1; i < 1001; i++){
        for (int j = 0; j < 1001; j++){
            A[i][j] += A[i-1][j];
        }
    }
    for (int i = 0; i < 1001; i++){
        for (int j = 1; j < 1001; j++){
            A[i][j] += A[i][j-1];
        }
    }
    vi ans(N+1);
    for (int i = 0; i < 1001; i++){
        for (int j = 0; j < 1001; j++){
            ans[A[i][j]]++;
        }
    }
    for (int i = 1; i <= N; i++){
        cout << ans[i] << endl;
    }
}