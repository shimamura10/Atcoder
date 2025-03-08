#include<bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    int Mg;
    cin >> Mg;
    vector<vector<bool>> gridg(N, vector<bool>(N, false));
    for (int i = 0; i < Mg; i++) {
        int u, v;
        cin >> u >> v;
        gridg[u-1][v-1] = true;
        gridg[v-1][u-1] = true;
    }
    int Mh;
    cin >> Mh;
    vector<vector<bool>> gridh(N, vector<bool>(N, false));
    for (int i = 0; i < Mh; i++) {
        int u, v;
        cin >> u >> v;
        gridh[u-1][v-1] = true;
        gridh[v-1][u-1] = true;
    }
    vector<vector<int>> A(N, vector<int>(N, 0));
    for (int i=0; i<N; i++) {
        for (int j=i+1; j<N; j++) {
            int a;
            cin >> a;
            A[i][j] = a;
            A[j][i] = a;
        }
    }

    vector<int> mapping(N);
    for (int i=0; i<N; i++) {
        mapping[i] = i;
    }

    long long ans = LLONG_MAX;
    do
    {
        long long tmp = 0;
        for (int i=0; i<N; i++) {
            for (int j=i+1; j<N; j++) {
                if (gridh[i][j] != gridg[mapping[i]][mapping[j]]) {
                    tmp += A[i][j];
                }
            }
        }
        ans = min(ans, tmp);
    } while (next_permutation(mapping.begin(), mapping.end()));
    
    cout << ans << endl;
}