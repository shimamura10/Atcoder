#include<bits/stdc++.h>
using namespace std;

int main() {
    int N, Q;
    cin >> N >> Q;
    vector<int> Pos(N);
    vector<int> Map(N);
    vector<int> Inv(N);
    for (int i=0; i<N; i++) {
        Pos[i] = i;
        Map[i] = i;
        Inv[i] = i;
    }

    for (int i=0; i<Q; i++) {
        int t;
        cin >> t;
        if (t == 1) {
            int a, b;
            cin >> a >> b;
            a--; b--;
            Pos[a] = Inv[b];
        } else if (t == 2) {
            int a, b;
            cin >> a >> b;
            a--; b--;
            swap(Map[Inv[a]], Map[Inv[b]]);
            swap(Inv[a], Inv[b]);
        } else if (t == 3) {
            int a;
            cin >> a;
            a--;
            cout << Map[Pos[a]] + 1 << endl;
        }

        // vector<vector<int>> tmp(N);
        // for (int i=0; i<N; i++) {
        //     tmp[Map[Pos[i]]].push_back(i);
        // }
        // for (int i=0; i<N; i++) {
        //     cout << i+1 << ": ";
        //     for (int j=0; j<tmp[i].size(); j++) {
        //         cout << tmp[i][j] + 1 << " ";
        //     }
        //     cout << endl;
        // }
        // cout << "Pos: ";
        // for (int i=0; i<N; i++) {
        //     cout << Pos[i] + 1 << " ";
        // }
        // cout << endl;
        // cout << "Map: ";
        // for (int i=0; i<N; i++) {
        //     cout << Map[i] + 1 << " ";
        // }
        // cout << endl;
        // cout << "Inv: ";
        // for (int i=0; i<N; i++) {
        //     cout << Inv[i] + 1 << " ";
        // }
        // cout << endl;
    }
}