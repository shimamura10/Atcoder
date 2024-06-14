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
using vi = vector<int>;
using vvi = vector<vector<int>>;
using vl = vector<long long>;

int main(){
    string S;
    cin >> S;
    unordered_map<char, int> count_s;
    for (const auto& s : S) {
        if (count_s.count(s) == 0) {
            count_s.emplace(s, 1);
        } else {
            count_s[s] += 1;
        }
    }

    for (int i=1; i<=S.size(); i++) {
        int count{0};
        for (const auto& [s, c] : count_s) {
            if (c == i) {
                count += 1;
            }
        }
        if (count != 0 && count != 2) {
            cout << "No";
            return 0;
        }
    }
    cout << "Yes";
}