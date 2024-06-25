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
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using vl = vector<long long>;

int main(){
    int N, M;
    cin >> N >> M;
    vi A{};
    for (int i=0; i<M; i++) {
        int a;
        cin >> a;
        A.emplace_back(a);
    }
    vvi X{};
    for (int i=0; i<N; i++) {
        vi tmp{};
        for (int j=0; j<M; j++) {
            int x;
            cin >> x;
            tmp.emplace_back(x);
        }
        X.emplace_back(tmp);
    }
    for (int j=0; j<M; j++) {
        auto & a = A[j];
        for (int i=0; i<N; i++) {
            a -= X[i][j];
        }
        if (a > 0) {
            cout << "No";
            return 0;
        }
    }
    cout << "Yes";
}