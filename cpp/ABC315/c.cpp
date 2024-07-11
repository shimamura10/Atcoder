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
    unordered_map<int, vi> mp;
    for (int i = 0; i < N; ++i){
        int f, s;
        cin >> f >> s;
        mp[f].push_back(s);
    }
    int M{0}, M2{0}, sameM{0};
    for (const auto& [k, v] : mp){
        int tmpM{0}, tmpM2{0};
        for (const auto& e : v){
            if (e > tmpM2) {
                if (e > tmpM){
                    tmpM2 = tmpM;
                    tmpM = e;
                } else {
                    tmpM2 = e;
                }
            }
        }
        if (tmpM > M2) {
            if (tmpM > M){
                M2 = M;
                M = tmpM;
            } else {
                M2 = tmpM;
            }
        }
        sameM = max(sameM, tmpM+tmpM2/2);
    }
    cout << max(M+M2, sameM) << endl;
}