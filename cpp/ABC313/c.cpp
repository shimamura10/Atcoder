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

int main(){
    int N;
    cin >> N;
    vl A(N);
    for (int i=0; i<N; i++) {
        cin >> A[i];
    }
    ll ave = accumulate(A.begin(), A.end(), 0LL) / N;
    ll plus = 0, minus = 0;
    for (int i=0; i<N; i++) {
        if (A[i] > ave) {
            plus += A[i] - ave-1;
        } else {
            minus += ave - A[i];
        }
    }
    cout << max(plus, minus) << endl;
}