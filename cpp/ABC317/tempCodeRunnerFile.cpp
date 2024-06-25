int dfs(int v, int p, vi& dis){
//     int res = 0;
//     for (auto [u, w] : G[v]){
//         if (u == p) continue;
//         res = max(res, w + dfs(u, v, dis));
//     }
//     dis[v] = res;
//     return res;
// }