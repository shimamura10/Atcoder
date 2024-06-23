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

vector<string> S{};

bool check_TaK(int x, int y) {
    for (int i=0; i<3; i++) {
        for (int j=0; j<3; j++) {
            if (S[x+i][y+j] == '.') {
                return false;
            }
            if (S[x+8-i][y+8-j] == '.') {
                return false;
            }
        }
    }

    for (int i=0; i<4; i++) {
        if (S[x+3][y+i] == '#') {
            return false;
        }
        if (S[x+i][y+3] == '#') {
            return false;
        }
        if (S[x+5][y+8-i] == '#') {
            return false;
        }
        if (S[x+8-i][y+5] == '#') {
            return false;
        }
    }

    return true;
}

int main(){
    int N, M;
    cin >> N >> M;
    for (int i=0; i<N; i++) {
        string s;
        cin >> s;
        S.push_back(s);
    }

    for (int i=0; i<N-8; i++) {
        for (int j=0; j<M-8; j++) {
            if (check_TaK(i, j)) {
                cout << i+1 << " " << j+1 << endl;
            }
        }
    }
}