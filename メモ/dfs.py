#各頂点を親とした部分木に含まれる要素数を求める
n = [0]*N
def dfs(v,pv):
    res = 1
    for j in G[v]:
        if j == pv:
            continue
        res += dfs(j,v)
    n[v] = res
    return res
