#include <iostream>
#include <algorithm>
#include <vector>
#include <functional>
using namespace std;

int main(){
    int Q;
    cin >> Q;
    vector<int> A;
    for (int i = 0; i < Q; i++)
    {
        int sig, n;
        cin >> sig >> n;
        switch (sig)
        {
        case 1:
            A.emplace_back(n);
            break;
        case 2:
            cout << A[A.size()-n] << "\n";
        default:
            break;
        }
    }
}