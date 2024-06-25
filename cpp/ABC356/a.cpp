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

int main(){
    int N, L, R;
    cin >> N >> L >> R;
    for (int i=1; i<L; i++) {
        cout << i << " ";
    } 
    for (int i=R; i>=L; i--) {
        cout << i << " ";
    }
    for (int i=R+1; i<=N; i++) {
        cout << i << " ";
    }
}