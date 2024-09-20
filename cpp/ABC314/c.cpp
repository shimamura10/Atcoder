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
    int N, M;
    cin >> N >> M;
    string S;
    cin >> S;
    unordered_map<int, vector<int>> v;
    for (int i = 0; i < N; i++){
        int c;
        cin >> c;
        v[c].push_back(i);
    }
    auto ans = S;
    for (const auto& p : v){
        int c = p.first;
        auto n = p.second.size();
        for (int i = 0; i < n; i++){
            ans[p.second[(i+1)%n]] = S[p.second[i]];
        }
    }
    cout << ans << endl;
}