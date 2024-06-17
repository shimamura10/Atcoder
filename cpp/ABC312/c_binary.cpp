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

vi A, B;
int N, M;

int binary_search(function<bool(int)> f, int l, int r){
    while (r-l > 1){
        int m = l + (r-l)/2;
        if (f(m)){
            r = m;
        } else {
            l = m;
        }
    }
    return r;
}

bool f(int x) {
    int cnt_sell{static_cast<int>(lower_bound(A.begin(), A.end(), x+1) - A.begin())};
    int cnt_buy{M - static_cast<int>(lower_bound(B.begin(), B.end(), x) - B.begin())};
    return cnt_sell >= cnt_buy;
}

int main(){
    cin >> N >> M;
    for (int i=0; i<N; i++) {
        int a;
        cin >> a;
        A.push_back(a);
    }
    for (int i=0; i<M; i++) {
        int b;
        cin >> b;
        B.push_back(b);
    }
    sort(A.begin(), A.end());
    sort(B.begin(), B.end());
    cout << binary_search(f, 0, 1000000001) << endl;
}