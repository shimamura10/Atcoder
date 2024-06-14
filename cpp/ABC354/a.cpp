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
    int H;
    cin >> H;
    ll grow{1};
    ll plant{0};
    for (int i=1; i<50; i++) {
        plant += grow;
        if (H < plant) {
            cout << i << endl;
            return 0;
        }
        grow *= 2;
    }
}