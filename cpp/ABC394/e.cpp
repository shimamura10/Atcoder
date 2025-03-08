#include<bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<vector<char>> C(N, vector<char>(N));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> C[i][j];
        }
    }

    vector<vector<pair<int, int>>> edges(N*N+1);
    for (int i=0; i<N; i++) {
        edges[N*N].emplace_back(i*N+i, 0);
    }
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            if (C[i][j] != '-') {
                edges[N*N].emplace_back(i*N+j, 1);
            }
        }
    }
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            for (int k=0; k<N; k++) {
                for (int l=0; l<N; l++) {
                    if (C[k][i] != '-' && C[j][l] != '-' && C[k][i] == C[j][l]) {
                        edges[i*N+j].emplace_back(k*N+l, 2);
                    }
                }
            }
        }
    }

    vector<vector<int>> dist(N+1, vector<int>(N, -1));
    dist[N][0] = 0;
    vector<int> stack(1, N*N);
    while (!stack.empty()) {
        int v = stack.back();
        auto i = v/N;
        auto j = v%N;
        stack.pop_back();
        for (auto [u, c] : edges[v]) {
            auto ni = u/N;
            auto nj = u%N;
            if (dist[ni][nj] == -1 || dist[ni][nj] > dist[i][j] + c) {
                dist[ni][nj] = dist[i][j] + c;
                stack.push_back(u);
            }
        }
    }
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cout << dist[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}