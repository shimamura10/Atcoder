#include<bits/stdc++.h>
using namespace std;

float time(int x1, int y1, int x2, int y2, int S) {
    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)) / S;
}

int main() {
    int N, S, T;
    cin >> N >> S >> T;
    vector<vector<int>> zahyo(N, vector<int>(4));
    float timeT;
    for (int i = 0; i < N; i++) {
        cin >> zahyo.at(i).at(0) >> zahyo.at(i).at(1) >> zahyo.at(i).at(2) >> zahyo.at(i).at(3);
        timeT += time(zahyo.at(i).at(0), zahyo.at(i).at(1), zahyo.at(i).at(2), zahyo.at(i).at(3), T);
    }
    vector<int> perm(N);
    iota(perm.begin(), perm.end(), 0);
    float ans = 2000*N/S;
    do {
        // cout << "perm: ";
        // for (int i = 0; i < N; i++) {
        //     cout << perm.at(i) << " ";
        // }
        // cout << endl;
        for (int bit = 0; bit < (1 << N); bit++) {
            float timeS = 0;
            if (bit & 1) {
                timeS += time(0, 0, zahyo.at(perm.at(0)).at(0), zahyo.at(perm.at(0)).at(1), S);
            } else {
                timeS += time(0, 0, zahyo.at(perm.at(0)).at(2), zahyo.at(perm.at(0)).at(3), S);
            }
            for (int i = 0; i < N-1; i++) {
                if (bit & (1 << i)) {
                    if (bit & (1 << i+1)) {
                        timeS += time(zahyo.at(perm.at(i)).at(2), zahyo.at(perm.at(i)).at(3), zahyo.at(perm.at(i+1)).at(0), zahyo.at(perm.at(i+1)).at(1), S);
                    } else {
                        timeS += time(zahyo.at(perm.at(i)).at(2), zahyo.at(perm.at(i)).at(3), zahyo.at(perm.at(i+1)).at(2), zahyo.at(perm.at(i+1)).at(3), S);
                    }
                } else {
                    if (bit & (1 << i+1)) {
                        timeS += time(zahyo.at(perm.at(i)).at(0), zahyo.at(perm.at(i)).at(1), zahyo.at(perm.at(i+1)).at(0), zahyo.at(perm.at(i+1)).at(1), S);
                    } else {
                        timeS += time(zahyo.at(perm.at(i)).at(0), zahyo.at(perm.at(i)).at(1), zahyo.at(perm.at(i+1)).at(2), zahyo.at(perm.at(i+1)).at(3), S);
                    }
                }
            }
            ans = min(ans, timeS);
            // cout << "timeS: " << timeS << " ans: " << ans << endl;
        }
    } while (next_permutation(perm.begin(), perm.end()));
    // 小数点以下7桁まで表示
    cout << fixed << setprecision(7);
    cout << ans + timeT << endl;
}