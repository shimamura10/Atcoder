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

template <typename T>
class Dijkstra
{
private:
    class Edge
    {
    public:
        T _to;
        ll _cost;
        Edge(T to, ll cost) : _to(to), _cost(cost) {};
    };
    unordered_map<T, vector<Edge>> _graph;
    unordered_set<T> _nodes;
    unordered_map<T, T> _preNode;
    T _start;
public:
    Dijkstra() {};

    void addEdge(T from, T to, ll cost)
    {
        _graph[from].emplace_back(to, cost);
        _nodes.insert(from);
        _nodes.insert(to);
    }

    unordered_map<T, ll> shortestDistance(T start)
    {
        priority_queue<tuple<ll, T>, vector<tuple<ll, T>>, greater<tuple<ll, T>>> heapq;
        unordered_map<T, ll> distances;
        for (auto node : _nodes)
        {
            distances[node] = LLONG_MAX;
        }
        distances[start] = 0;
        heapq.push(make_tuple(0, start));

        while (!heapq.empty())
        {
            ll cost;
            T now;
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

    vector<T> shortestPath(T goal)
    {
        vector<T> path;
        while (goal != _start)
        {
            path.emplace_back(goal);
            goal = _preNode[goal];
        }
        path.emplace_back(goal);

        return path;
    }
};

int main(){
    int N, M;
    cin >> N >> M;
    Dijkstra<int> dijkstra;
    for (int i=0; i<M; ++i){
        int a, b;
        ll c;
        cin >> a >> b >> c;
        a--; b--;
        dijkstra.addEdge(a, b, c);
        dijkstra.addEdge(b, a, c);
    }

    auto distances_from0 = dijkstra.shortestDistance(0);
    auto distances_fromN = dijkstra.shortestDistance(N-1);
    for (int i=0; i<N; ++i){
        cout << distances_from0[i] + distances_fromN[i] << endl;
    }
}