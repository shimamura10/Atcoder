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
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using vl = vector<long long>;

class Trie {
public:
    int ans{0};
    Trie(int len, int kind) {
        def.assign(kind, -1);
        edge.emplace_back(def);
        now_sz = 0;
        values.emplace_back(0);
    }

    void add_edge(const string &str) {
        int tmp_sz = 0;
        for (auto s : str) {
            int num = s - 'a';
            if (edge[tmp_sz][num] == -1) {
                edge[tmp_sz][num] = ++now_sz;
                tmp_sz = now_sz;
                edge.emplace_back(def);
                values.emplace_back(1);
            } else {
                tmp_sz = edge[tmp_sz][num];
                ans += values[tmp_sz]++;
            }
        }
    }
private:
    int now_sz;
    vi def;
    vvi edge;
    vi values;
};

int main(){
    int N;
    cin >> N;
    vector<string> S;
    for (int i=0; i<N; i++) {
        string s;
        cin >> s;
        S.emplace_back(s);
    }

    Trie trie{N, 26};
    for (auto str : S) {
        trie.add_edge(str);
    }

    cout << trie.ans;
}