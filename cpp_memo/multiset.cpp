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
    multiset<int> s = {1,1,2,2,3};
    auto it = s.find(2);
    s.erase(it, next(it));
    for (auto a : s) {
        cout << a << endl;
    }
}