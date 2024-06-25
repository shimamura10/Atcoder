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
    int N;
    cin >> N;
    vi A;
    vi posA(N, -1);
    for (int i=0; i<N; i++) {
        int a;
        cin >> a;
        a--;
        A.emplace_back(a);
        posA[a] = i;
    }

    vector<pair<int, int>> ans{};
    for (int i=0; i<N; i++) {
        if (posA[i] == i) { continue; }
        int posi = posA[i];
        int valj = A[i];
        A[posi] = valj;
        posA[valj] = posi;
        ans.emplace_back(i, posi);
    }

    cout << ans.size() << endl;
    for (auto& a : ans) {
        cout << a.first+1 << " " << a.second+1 << endl;
    }
}