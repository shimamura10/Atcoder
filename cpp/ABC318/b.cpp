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
    vvi A(101, vi(101, 0));
    for (int i = 0; i < N; ++i){
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        for (int x = a; x < b; ++x){
            for (int y = c; y < d; ++y){
                A[x][y] = 1;
            }
        }
    }
    cout << "";
    cout << accumulate(A.begin(), A.end(), 0, [](int acc, const vi& v){
        return acc + accumulate(v.begin(), v.end(), 0);
    }) << endl;
}