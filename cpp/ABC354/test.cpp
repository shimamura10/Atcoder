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
    int ans{1};
    for (int i=1; i<=9; i++) {
        ans *= i*i;
    }
    cout << (26 << 0) << endl;
    cout << (!(2 & 1)) << endl;
    cout << ans;
}