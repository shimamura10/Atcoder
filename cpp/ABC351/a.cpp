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
    int a{0}, b{0};
    for (int i=0; i<9; ++i){
        int c;
        cin >> c;
        a += c;
    }
    for (int i=0; i<8; ++i){
        int c;
        cin >> c;
        b += c;
    }
    cout << a - b + 1;
}