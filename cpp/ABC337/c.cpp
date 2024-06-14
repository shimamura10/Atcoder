#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    int N;
    cin >> N;
    
    vector<int> edge(N);
    int head;
    for (auto i = 0; i < N; i++)
    {
        int a;
        cin >> a;
        if (a == -1)
        {
            head = i;
        } else
        {
            edge[a-1] = i;
        }
    }
    cout << head + 1 << " ";
    for (auto _ = 0; _ < N-1; _++)
    {
        head = edge[head];
        cout << head + 1 << " ";
    }
}