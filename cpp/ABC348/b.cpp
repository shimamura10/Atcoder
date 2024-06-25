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
using namespace std;
using ll = long long;

ll distance2(const int& x, const int& y) {
    return x*x + y*y;
}

int main(){
    int N;
    cin >> N;
    vector<pair<int, int>> coordinate;
    for (int i=0; i<N; i++) {
        int x, y;
        cin >> x >> y;
        coordinate.push_back(make_pair(x,y));
    }

    for (const auto& [x1, y1] : coordinate) {
        int j{0};
        int ans{0};
        int max_dis{0};
        for (const auto& [x2, y2] : coordinate) {
            j++;
            auto tmp_dis = distance2(x1-x2, y1-y2);
            if (max_dis < tmp_dis) {
                ans = j;
                max_dis = tmp_dis;
            }
        }
        cout << ans << endl;
    }
}