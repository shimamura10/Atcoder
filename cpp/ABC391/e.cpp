#include<bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<vector<pair<int, int>>> A(N+1);
    vector<pair<int, int>> B{};
    string s;
    cin >> s;
    for (int i=0; i<(int)pow(3, N); i++) {
        B.emplace_back(static_cast<int>(s[i] - '0'), 1);
    }
    A[0] = B;
    for (int i=1; i<N+1; i++) {
        vector<pair<int, int>> tmp{};
        for (int j=0; j<(int)A[i-1].size()/3; j++) {
            int sum = 0;
            vector<pair<int, int>> tmp2;
            for (int k=0; k<3; k++) {
                sum += A[i-1][3*j+k].first;
                tmp2.emplace_back(A[i-1][3*j+k].first, A[i-1][3*j+k].second);
            }
            sort(tmp2.begin(), tmp2.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
                return a.second < b.second;
            });
            int cost = 0;
            int cnt = 0;
            switch (sum)
            {
                case 0:
                    cnt = 2;
                    for (int k=0; k<3; k++) {
                        if (tmp2[k].first == 0 && cnt > 0) {
                            cnt--;
                            cost += tmp2[k].second;
                        }
                    }
                    tmp.emplace_back(0, cost);
                    break;
                case 1:
                    cnt = 1;
                    for (int k=0; k<3; k++) {
                        if (tmp2[k].first == 0 && cnt > 0) {
                            cnt--;
                            cost += tmp2[k].second;
                        }
                    }
                    tmp.emplace_back(0, cost);
                    break;
                case 2:
                    cnt = 1;
                    for (int k=0; k<3; k++) {
                        if (tmp2[k].first == 1 && cnt > 0) {
                            cnt--;
                            cost += tmp2[k].second;
                        }
                    }
                    tmp.emplace_back(1, cost);
                    break;
                case 3:
                    cnt = 2;
                    for (int k=0; k<3; k++) {
                        if (tmp2[k].first == 1 && cnt > 0) {
                            cnt--;
                            cost += tmp2[k].second;
                        }
                    }
                    tmp.emplace_back(1, cost);
                    break;
                default:
                    break;
            }
        }
        A[i] = tmp;
    }

    cout << A[N][0].second << endl;
}