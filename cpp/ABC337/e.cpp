#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    int N;
    cin >> N;
    int M = 0;
    while (true)
    {
        if (1 << ++M >= N)
        {
            break;
        }
    }
    cout << M << endl;

    vector<vector<int>> A(M, vector<int>(N, 0));
    for (int n = 0; n < N; n++)
    {
        for (int m = 0; m < M; m++)
        {
            if (n>>m & 1)
            {
                A[m][n] = 1;
            }
        }
    }
    for (int m = 0; m < M; m++)
    {
        vector<int> a;
        int k = 0;
        for (int n = 0; n < N; n++)
        {
            if (A[m][n] == 1)
            {
                a.emplace_back(n+1);
                k++;
            }
        }
        cout << k;
        for (auto b : a)
        {
            cout << " " << b;
        }
        cout << endl;
    }
    
    string S;
    cin >> S;
    int X = 0;
    for (int m = 0; m < M; m++)
    {
        if (S[m] == '1')
        {
            X += 1 << m;
        }
    }
    cout << X+1;
}