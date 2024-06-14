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
    vi edges;
    vi inputCounts(N, 0);
    for (int i=0; i<N; i++) {
        int a;
        cin >> a;
        a--;
        edges.emplace_back(a);
        inputCounts[i]++;
    }

    vector<bool> visited(N, false);
    vi parents(N, -1);
    for (int i=0; i<N; i++) {
        if (visited[i]) { continue; }
        int next{edges[i]};
        while (parents[next] == -1) {
            parents[next] = i;
            next = edges[next];
        }
        if (parents[next] == i) {
            int start{next};
            int next2{edges[start]}
        }
    }
    unordered_map<int, int> circles;
}