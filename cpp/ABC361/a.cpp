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
    int N, K, X;
    cin >> N >> K >> X;
    for (int i=0; i<N; i++) {
        int a;
        cin >> a;
        cout << a << " ";
        if (i == K-1) {
            cout << X << " ";
        }
    }
}