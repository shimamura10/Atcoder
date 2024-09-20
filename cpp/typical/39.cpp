#include<bits/stdc++.h>
using namespace std;

void count_child(int parent, int node, vector<vector<int>>& tree, vector<int>& child_count)
{
    child_count[node] = 1;
    for (const auto& child : tree[node])
    {
        if (child == parent)
        {
            continue;
        }
        count_child(node, child, tree, child_count);
        child_count[node] += child_count[child];
    }
}

long long culc_root_dist(int parent, int node, vector<vector<int>>& tree, vector<int>& child_count)
{
    long long res = 0;
    for (const auto& child : tree[node])
    {
        if (child == parent)
        {
            continue;
        }
        res += culc_root_dist(node, child, tree, child_count) + child_count[child];
    }
    return res;
}

void culc_dist(int parent, int node, vector<vector<int>>& tree, vector<int>& child_count, vector<long long>& culc_dist_list)
{
    if (parent != -1) {
        culc_dist_list[node] = culc_dist_list[parent] + (tree.size() - 2*child_count[node]);
    }
    for (const auto& child : tree[node])
    {
        if (child == parent)
        {
            continue;
        }
        culc_dist(node, child, tree, child_count, culc_dist_list);
    }
}

int main()
{
    int n;
    cin >> n;
    vector<vector<int>> tree(n);
    for (int i = 0; i < n-1; i++)
    {
        int a, b;
        cin >> a >> b;
        a--;
        b--;
        tree[a].push_back(b);
        tree[b].push_back(a);
    }

    vector<int> child_count(n);
    count_child(-1, 0, tree, child_count);

    vector<long long> culc_dist_list(n);
    culc_dist_list[0] = culc_root_dist(-1, 0, tree, child_count);
    culc_dist(-1, 0, tree, child_count, culc_dist_list);

    cout << accumulate(culc_dist_list.begin(), culc_dist_list.end(), 0LL)/2 << endl;

    return 0;
}