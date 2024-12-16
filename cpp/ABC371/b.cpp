#include<bits/stdc++.h>
using namespace std;

int main()
{
    int N, M;
    cin >> N >> M;
    vector<bool> isFirst(N, true);
    for (int i=0; i<M; i++) {
        int A;
        char B;
        cin >> A >> B;
        if (B == 'M') {
            if (isFirst[A-1]) {
                cout << "Yes" << endl;
                isFirst[A-1] = false;
                continue;
            }
        }
        cout << "No" << endl;
    }
}