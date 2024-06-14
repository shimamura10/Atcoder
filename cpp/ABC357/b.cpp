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

void switchUpLow(char& a) {
    if (a - 'a' >= 0) {
        a = static_cast<char>(a - 'a' + 'A');
    } else {
        a = static_cast<char>(a - 'A' + 'a');
    }
}

int main(){
    string S;
    cin >> S;
    int cntLow{0};
    for (auto s : S) {
        if (s - 'a' >= 0) {
            cntLow++;
        } else {
            cntLow--;
        }
    }
    if (cntLow > 0) {
        for (auto s : S) {
            if (s - 'a' < 0) {
                switchUpLow(s);
            }
            cout << s;
        }
    } else {
        for (auto s : S) {
            if (s - 'a' >= 0) {
                switchUpLow(s);
            }
            cout << s;
        }
    }
}