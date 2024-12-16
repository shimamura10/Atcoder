#include<bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> H(N);
    for (int i=0; i<N; i++) {
        cin >> H[i];
    }

    vector<int> stack{};
    stack.push_back(H.back());
    vector<int> ans(N, 0);
    for (int i=N-2; i>=0; i--) {
        ans[i] = stack.size();
        while (!stack.empty() && stack.back() < H[i]) {
            stack.pop_back();
        }
        stack.push_back(H[i]); 
    }

    for (int i=0; i<N; i++) {
        cout << ans[i] << " ";
    }
}