#include<bits/stdc++.h>
using namespace std;

class State{
    public:
    int u;
    long long d;
    bool rev;
    State(int u, long long d, bool rev) : u(u), d(d), rev(rev) {}
    bool operator>(const State& s) const {
        return d > s.d;
    }
};

int main() {
    int N, M;
    long long X;
    cin >> N >> M >> X;
    vector<vector<int>> G(N);
    vector<vector<int>> revG(N);
    for (int i = 0; i < M; i++) {
        int u, v;
        cin >> u >> v;
        u--; v--;
        G[u].push_back(v);
        revG[v].push_back(u);
    }

    priority_queue<State, vector<State>, greater<State>> pq;
    vector<long long> dist(N, 1e18);
    vector<long long> revDist(N, 1e18);
    pq.push(State(0, 0, false));
    dist[0] = 0;
    revDist[0] = 0;
    while (!pq.empty()) {
        auto s = pq.top();
        pq.pop();
        if (s.u == N - 1) {
            cout << s.d << endl;
            return 0;
        }
        if (!s.rev && (dist[s.u] < s.d)) continue;
        if (s.rev && (revDist[s.u] < s.d)) continue;
        for (int v : G[s.u]) {
            auto cost = (s.rev ? X : 0) + 1;
            auto& nowDist = s.rev ? revDist : dist;
            if (dist[v] > nowDist[s.u] + cost) {
                dist[v] = nowDist[s.u] + cost;
                pq.push(State(v, dist[v], false));
            }
        }
        for (int v : revG[s.u]) {
            auto cost = (s.rev ? 0 : X) + 1;
            auto& nowDist = s.rev ? revDist : dist;
            if (revDist[v] > nowDist[s.u] + cost) {
                revDist[v] = nowDist[s.u] + cost;
                pq.push(State(v, revDist[v], true));
            }
        }
    }
}