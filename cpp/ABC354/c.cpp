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
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using vl = vector<long long>;

struct Card
{
    int power;
    int cost;
    Card(const int& power, const int& cost) : power{power}, cost{cost} {}
    // bool operator<(const Card& rhs) const {

    // }
};

bool comp(const pair<int, int>& lhs, const pair<int, int>& rhs) {
    return lhs.first < rhs.first;
}

int main(){
    int N;
    cin >> N;
    vector<pair<int, int>> powers;
    vector<pair<int, int>> costs;
    for (int i=0; i<N; i++) {
        int a, c;
        cin >> a >> c;
        powers.emplace_back(-a, i);
        costs.emplace_back(c, i);
    }
    sort(powers.begin(), powers.end(), comp);
    sort(costs.begin(), costs.end(), comp);

    vector<bool> rests(N, true);
    for (auto& power : powers) {
        if (!rests[power.second]) {continue;}
        while (true) {
            auto tmp = costs.back();
            costs.pop_back();
            if (power.second == tmp.second) {
                break;
            }
            rests[tmp.second] = false;
        }
    }
    vi ans{};
    for (int i=0; i<N; i++) {
        if (rests[i]) {
            ans.push_back(i+1);
        }
    }
    cout << ans.size() << endl;
    for (auto& a : ans) {
        cout << a << " ";
    }
}