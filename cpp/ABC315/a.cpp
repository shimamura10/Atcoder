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
    string S;
    cin >> S;
    unordered_set<char> st{'a', 'i', 'u', 'e', 'o'};
    string ans{};
    for (const auto& c : S){
        if (st.find(c) == st.end()){
            ans += c;
        }
    }
    cout << ans << endl;
}