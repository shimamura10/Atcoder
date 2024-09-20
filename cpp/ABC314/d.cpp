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
    int Q;
    cin >> Q;
    vector<pair<int, char>> task1;
    int task2 = 0;
    for (int i = 0; i < Q; i++){
        int t, x;
        char c;
        cin >> t >> x >> c;
        if (t == 1){
            task1.emplace_back(x-1, c);
        } else {
            for (auto& p : task1){
                S[p.first] = p.second;
            }
            task1.clear();
            if (t == 2) {
                task2 = 2;
            } else if (t == 3) {
                task2 = 3;
            }
        }
    }


    if (task2 == 2){
        for (auto& s : S) {
            if (s - 'A' >= 0 && s - 'Z' <= 0) {
                s = static_cast<char>(s - 'A' + 'a');
            }
        }
    } else if (task2 == 3){
        for (auto& s : S) {
            if (s - 'a' >= 0 && s - 'z' <= 0) {
                s = static_cast<char>(s - 'a' + 'A');
            }
        }
    }

    for (auto& p : task1){
        S[p.first] = p.second;
    }
    task1.clear();

    cout << S << endl;
}