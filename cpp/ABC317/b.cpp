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
    vi A(N);
    for(int i = 0; i < N; ++i){
        cin >> A[i];
    }
    sort(A.begin(), A.end());
    for (int i = 0; i<N; ++i){
        if (i+A[0] != A[i]) {
            cout << i+A[0] << endl;
            return 0;
        }
    }
}