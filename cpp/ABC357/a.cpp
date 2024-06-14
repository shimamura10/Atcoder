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
    for (int i=0; i<N; i++) {
        int h;
        cin >> h;
        M -= h;
        if (M < 0) {
            cout << i;
            return 0;
        }
    }
    cout << N;
}