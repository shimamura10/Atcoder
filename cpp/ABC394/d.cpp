#include<bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    unordered_map<char, int> mp = {
        {'(', 1},
        {')', -1},
        {'<', 2},
        {'>', -2},
        {'[', 3},
        {']', -3}
    };
    vector<char> stack;
    for (int i=0; i<S.size(); i++) {
        if (mp[S[i]] > 0) {
            stack.push_back(S[i]);
        } else {
            if (stack.empty()) {
                cout << "No" << endl;
                return 0;
            }
            if (mp[S[i]] + mp[stack.back()] == 0) {
                stack.pop_back();
            } else {
                cout << "No" << endl;
                return 0;
            }
        }
    }
    if (!stack.empty()) {
        cout << "No" << endl;
        return 0;
    }
    cout << "Yes" << endl;
    return 0;
}