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

class Dijkstra
{
private:
    class Edge
    {
    public:
        int _to;
        ll _cost;
        Edge(int to, ll cost) : _to(to), _cost(cost) {};
    };
    vector<vector<Edge>> _graph;
    int _nodeNum;
    unordered_map<int, int> _preNode;
    int _start;
public:
    Dijkstra(int nodeNum)
    {
        _nodeNum = nodeNum;
        _graph.resize(nodeNum);
    }

    void addEdge(int from, int to, ll cost)
    {
        _graph[from].emplace_back(to, cost);
    }

    vector<ll> shortestDistance(int start)
    {
        priority_queue<tuple<ll, int>, vector<tuple<ll, int>>, greater<tuple<ll, int>>> heapq;
        vector<ll> distances(_nodeNum);
        for (int node=0; node<_nodeNum; node++)
        {
            distances[node] = LLONG_MAX;
        }
        distances[start] = 0;
        heapq.push(make_tuple(0, start));

        while (!heapq.empty())
        {
            ll cost;
            int now;
            tie(cost, now) = heapq.top();
            heapq.pop();

            if (distances[now] < cost) {continue;}

            for (Edge edge : _graph[now])
            {
                if (distances[edge._to] > distances[now] + edge._cost)
                {
                    distances[edge._to] = distances[now] + edge._cost;
                    _preNode[edge._to] = now;
                    heapq.push(make_tuple(distances[edge._to], edge._to));
                }
            }
        }
        
        _start = start;
        return distances;
    };
};

ll calc_children_costs(int parent, int root, const vvi& edge, const vector<ll>& cost_list, vector<ll>& cache) {
    ll cost = cost_list[root];
    for (const auto& child : edge[root]) {
        if (child == parent) { continue; }
        cost += calc_children_costs(root, child, edge, cost_list, cache);
    }
    cache[root] = cost;
    return cost;
}

void calc_f(int parent, int me, const vvi& edge,const ll& all_cost, const vector<ll>& children_costs, vector<ll>& cache) {
    if (parent != me) {
        cache[me] = cache[parent] - 2*children_costs[me] + all_cost;
    }
    for (const auto& child : edge[me]) {
        if (child == parent) { continue; }
        calc_f(me, child, edge, all_cost, children_costs, cache);
    }
}

int main(){
    int N;
    cin >> N;
    vvi edge(N);
    Dijkstra dijkstra(N);
    for (int i=0; i<N-1; i++) {
        int a, b;
        cin >> a >> b;
        a--;
        b--;
        edge[a].emplace_back(b);
        edge[b].emplace_back(a);
        dijkstra.addEdge(a,b,1);
        dijkstra.addEdge(b,a,1);
    }
    vector<ll> cost_list;
    for (int i=0; i<N; i++) {
        ll c;
        cin >> c;
        cost_list.emplace_back(c);
    }

    vector<ll> children_costs(N);
    calc_children_costs(0, 0, edge, cost_list, children_costs);

    auto distance_from_root = dijkstra.shortestDistance(0);
    ll f_root = 0LL;
    for (int i=0; i<N; i++) {
        f_root += cost_list[i]*distance_from_root[i];
    }

    auto all_cost = accumulate(cost_list.begin(), cost_list.end(), 0LL);
    vector<ll> f_list(N);
    f_list[0] = f_root;
    calc_f(0, 0, edge, all_cost, children_costs, f_list);

    cout << *min_element(f_list.begin(), f_list.end());
}