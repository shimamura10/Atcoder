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
    vector<pair<int, int>> Gigant;
    for (int i=0; i<N; ++i){
        int x, y;
        cin >> x >> y;
        Gigant.push_back(make_pair(x, y));
    }
    sort(Gigant.begin(), Gigant.end(), [](pair<int, int> a, pair<int, int> b){
        return a.second - a.first < b.second - b.first;
    });
    ll ans = 0;
    for (int i=0; i<N-1; ++i){
        ans += Gigant[i].first;
    }
    ans += Gigant[N-1].second;
    cout << ans << endl;
}