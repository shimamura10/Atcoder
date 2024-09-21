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

const string S = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679";

int main(){
    int N;
    cin >> N;
    // SのN+2文字目までを出力
    for(int i = 0; i < N+2; i++){
        cout << S[i];
    }
}