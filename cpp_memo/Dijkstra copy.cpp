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
using namespace std;
using lint = long long;

class Dijkstra
{
private:
    class Edge
    {
    public:
        int _to;
        lint _cost;
        Edge(int to, lint cost) : _to(to), _cost(cost) {};
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

    void addEdge(int from, int to, lint cost)
    {
        _graph[from].emplace_back(to, cost);
    }

    vector<lint> shortestDistance(int start)
    {
        priority_queue<tuple<lint, int>, vector<tuple<lint, int>>, greater<tuple<lint, int>>> heapq;
        vector<lint> distances(_nodeNum);
        for (int node=0; node<_nodeNum; node++)
        {
            distances[node] = LLONG_MAX;
        }
        distances[start] = 0;
        heapq.push(make_tuple(0, start));

        while (!heapq.empty())
        {
            lint cost;
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

    // vector<T> shortestPath(T goal)
    // {
    //     vector<T> path;
    //     while (true)
    //     {
    //         path.emplace_back(goal);
    //         goal = _preNode[goal];
    //         if (goal == _start) {break;}
    //     }
    //     return path;
    // }
};

int main(){
    
}