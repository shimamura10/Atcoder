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
    string S;
    cin >> S;
    int ans = -1;
    int tmp = -1;
    bool flag = false;
    for (const auto& c : S){
        if (c == '-'){
            flag = true;
            ans = max(ans, tmp);
            tmp = -1;
        } else {
            if (tmp == -1) tmp = 0;
            tmp++;
        }
    }
    if (flag){
        cout << max(ans, tmp) << endl;
    } else {
        cout << -1 << endl;
    }
}