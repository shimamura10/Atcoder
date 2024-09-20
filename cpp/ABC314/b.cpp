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
    int N;
    cin >> N;
    vector<vector<pair<int, int>>> v(37);
    for (int i = 0; i < N; i++){
        int c;
        cin >> c;
        for (int j=0; j<c; j++){
            int a;
            cin >> a;
            v[a].push_back({c, i+1});
        }
    }
    int x;
    cin >> x;
    auto vx = v[x];
    vi ans{};
    if (vx.size() != 0){
        auto minc = min_element(vx.begin(), vx.end())->first;
        for (auto p : vx){
            if (p.first == minc){
                ans.push_back(p.second);
            }
        }
    }

    cout << ans.size() << endl;
    for (auto a : ans){
        cout << a << " ";
    }
}