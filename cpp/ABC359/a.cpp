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
    string t = "Takahashi";
    int cnt = 0;
    for (int i = 0; i < N; ++i){
        string s;
        cin >> s;
        if (s == t){
            ++cnt;
        }
    }

    cout << cnt << endl;
}