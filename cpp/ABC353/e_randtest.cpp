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
#include <random>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using vl = vector<long long>;

std::random_device seed_gen;
std::default_random_engine engine(seed_gen());

uniform_int_distribution<> dist(0, 25);
uniform_int_distribution<> distN(2, 100);
uniform_int_distribution<> dist2(1, 100);


string generateRandStr(int n) {
    string ret = "";
    for (int i=0; i<n; i++) {
        ret += static_cast<char>(static_cast<int>('a') + dist(engine));
    }
    // cout << ret << endl;
    return ret;
}

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

struct trie {
  using ar = array<int, 26>;
  vector<ar> pos;
  ar def;
  int now_sz;
  long long ans;
  vector<int> cnt;
  trie() = default;
  trie(int len) {
    pos.reserve(len + 1);
    cnt.reserve(len + 1);
    def.fill(-1);
    now_sz = ans = 0;
    make_node();
  }
  int make_node() {
    pos.push_back(def);
    cnt.push_back(0);
    return now_sz++;
  }
  void add(string &s) {
    int now = 0;
    for(int i = 0; i < (int)s.size(); i++) {
      int d = s[i] - 'a';
      int &nx = pos[now][d];
      if(nx == -1)
        nx = make_node();
      now = nx;
      ans += cnt[now]++;
    }
  }
};


int main(){
    for (int i=0; i<1000; i++) {

    int N = distN(engine);
    vector<string> S;
    for (int i=0; i<N; i++) {
        string s{generateRandStr(dist2(engine))};
        S.emplace_back(s);
    }
    

    int ans1, ans2;

    Trie myTrie{N, 26};
    for (auto str : S) {
        myTrie.add_edge(str);
    }
    ans1 = myTrie.ans;
    

    // unordered_map<string, int> count_z;
    // ll ans = 0;
    // for (auto str : S) {
    //     string z = "";
    //     for (auto s : str) {
    //         z += s;
    //         if (count_z.count(z) == 0) {
    //             count_z[z] = 1;
    //         } else {
    //             ans += count_z[z];
    //             count_z[z] += 1;
    //         }
    //     }
    // }

    trie tr(300000);
    for (auto str : S) {
        tr.add(str);
    }
    ans2 = tr.ans;
    

    if (ans1 != ans2) {
        cout << "---Input---" << endl;
        cout << "N: " << N << endl;
        cout << "S" << endl;
        for (auto str : S) {
            cout << str << endl;
        }
        cout << "ans1: " << ans1 << endl;
        cout << "ans2: " << ans2 << endl;
    }
    }
}