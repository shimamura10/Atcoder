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

int fact3(int n) {
    static vi ret{1};
    while (ret.size() <= n) {
        ret.emplace_back(ret.back()*3);
    }
    return ret[n];
}

void plotCarpet(int level, int x, int y, vector<vector<char>>& carpet) {
    if (level == 0) {
        carpet[x][y]  = '#';
        return;
    }
    for (int i=0; i<3; i++) {
        for (int j=0; j<3; j++) {
            if (i==1 && j==1) {continue;}
            plotCarpet(level-1, x+fact3(level-1)*i, y+fact3(level-1)*j, carpet);
        }
    }
}

int main(){
    int N;
    cin >> N;
    vector<vector<char>> carpet(pow(3,N), vector<char>(pow(3,N), '.'));
    plotCarpet(N, 0, 0, carpet);
    for (const auto& row : carpet) {
        for (const auto& str : row) {
            cout << str;
        }
        cout << '\n';
    }
}