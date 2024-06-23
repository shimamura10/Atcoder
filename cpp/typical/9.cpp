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
#include <numbers>
#include <iomanip>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using vl = vector<long long>;
const ll MOD = 998244353;

double angle(pair<double, double> p1, pair<double, double> p2){
    return atan2(p2.second - p1.second, p2.first - p1.first)/numbers::pi*180;
}

double adjust_angle(double angle){
    auto ret = angle;
    if (ret < 0) {
        ret += 360;
    }
    if (ret >= 180) {
        ret = 360 - ret;
    }
    return ret;
}

int main(){
    int N;
    cin >> N;
    vector<pair<double, double>> Coordinates(N);
    for (int i=0; i<N; ++i){
        cin >> Coordinates[i].first >> Coordinates[i].second;
    }
    
    vector<vector<double>> angles(N);
    for (int i=0; i<N; ++i){
        for (int j=0; j<N; ++j){
            if (i == j) continue;
            angles[i].emplace_back(angle(Coordinates[i], Coordinates[j]));
        }
        sort(angles[i].begin(), angles[i].end());
    }

    double ans = 0;
    for (int i=0; i<N; ++i){
        for (const auto& angle : angles[i]){
            double anti_angle = angle + 180;
            if (anti_angle > 180) {
                anti_angle -= 360;
            }
            auto idx = lower_bound(angles[i].begin(), angles[i].end(), anti_angle) - angles[i].begin();
            ans = max(ans, adjust_angle(angles[i][idx%(N-1)] - angle));
            if (idx == 0) {
                ans = max(ans, adjust_angle(angles[i][N-2] - angle));
            } else {
                ans = max(ans, adjust_angle(angles[i][idx-1] - angle));
            }
        }
    }

    cout << fixed << setprecision(15) << ans << endl;
}