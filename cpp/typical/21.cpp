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
const ll MOD = 998244353;

// connにエッジを登録し、make_group()を呼ぶことでSCCを構築する
// https://qiita.com/fu2tian2/items/cb316c01c281bbe20452
struct SCC {
    ll n;
    // trueで登録するのは元の向きの枝
    // falseは逆向きの枝(dfs2で用いる)
    vector<vector<pair<ll,bool>>> conn;
    vector<ll> checked;
    vector<ll> orderList;
    vector<ll> groupList;
    ll cnt = 0;
    SCC(ll n) : n(n), conn(n), checked(n,0), orderList(n,-1), groupList(n,-1) {};
    void dfs(ll now, ll prev) {
        checked[now]=1;
        for (auto v : conn[now]) {
            if (checked[v.first]==1 || v.first==prev || v.second==false) continue;
            dfs(v.first,now);
        }
        orderList[cnt]=now; cnt++;
        return;
    }
    void dfs2(ll now, ll group) {
        groupList[now]=group;
        for (auto v : conn[now]) {
            if (groupList[v.first]!=-1 || v.second==true) continue;
            dfs2(v.first,group);
        }
        return;
    }
    void make_group() {
        for (int i=0; i < n; i++) {
            if (!checked[i]) dfs(i,-1);
        }
        for (int i=n-1; i>=0; i--) {
            if (orderList[i]==-1) break;
            if (groupList[orderList[i]]!=-1) continue;
            dfs2(orderList[i],orderList[i]);
        }
    }
};

int main(){
    int N, M;
    cin >> N >> M;
    SCC scc(N);
    for (int i = 0; i < M; i++)
    {
        int a, b;
        cin >> a >> b;
        a--; b--;
        scc.conn[a].emplace_back(b,true);
        scc.conn[b].emplace_back(a,false);
    }
    scc.make_group();
    unordered_map<ll, ll> groupSize;
    for (int i = 0; i < N; i++)
    {
        groupSize[scc.groupList[i]]++;
    }
    ll ans = 0;
    for (const auto& [k, v] : groupSize)
    {
        ans += v*(v-1)/2;
    }

    cout << ans << endl;
}