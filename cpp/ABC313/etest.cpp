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
    string S;
    cin >> S;
    int cnt{0};
    while (S.size() > 1) {
        string T{};
        for (int i = 0; i < S.size()-1; i++) {
            for (int j = 0; j < static_cast<int>(S[i+1] - '0'); j++) {
                T.push_back(S[i]);
            }
        }
        S = T;
        cnt++;
        cout << S << endl;
    }
}