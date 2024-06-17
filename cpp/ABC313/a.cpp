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
    vi P(N);
    for (int i=0; i<N; i++) {
        cin >> P[i];
    }
    auto M{max_element(P.begin()+1, P.end())};
    if (P.front() > *M)
        cout << 0 << endl;
    else
        cout << *M - P.front() + 1 << endl;
}