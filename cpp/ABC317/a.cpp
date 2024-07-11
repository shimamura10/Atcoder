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
    int N, H, X;
    cin >> N >> H >> X;
    for(int i = 0; i < N; ++i){
        int p;
        cin >> p;
        if (p + H >= X){
            cout << i+1 << endl;
            return 0;
        }
    }
}