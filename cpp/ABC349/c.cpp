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
    string S, T;
    cin >> S >> T;
    transform(T.begin(), T.end(), T.begin(), ::tolower);
    int index{0};
    for (const auto& s : S) {
        if (s == T[index]) {
            index++;
            if (index == 3) {
                cout << "Yes";
                return 0;
            }
        }
    }

    if (index == 2 && T[2] == 'x') {
        cout << "Yes";
        return 0;
    }
    cout << "No";
}