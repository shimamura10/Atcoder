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
    int N, X, Y, Z;
    cin >> N >> X >> Y >> Z;
    if (X > Y) {
        swap(X, Y);
    }
    if (X < Z && Z < Y) {
        cout << "Yes";
    } else {
        cout << "No";
    }
}