#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    int H, W, K;
    cin >> H >> W >> K;
    vector<string> S;
    for (int i = 0; i < H; i++)
    {
        string s;
        cin >> s;
        S.emplace_back(s);
    }
    
    int ans = K+1;
    for (int h = 0; h < H; h++)
    {
        int circle = 0, dot = 0;
        for (int w = 0; w < min(W,K-1); w++)
        {
            if (S[h][w] == 'o')
            {
                circle += 1;
            } else if (S[h][w] == '.')
            {
                dot += 1;
            }
        }
        for (int w = K-1; w < W; w++)
        {
            if (S[h][w] == 'o')
            {
                circle += 1;
            } else if (S[h][w] == '.')
            {
                dot += 1;
            }

            if (circle + dot == K)
            {
                ans = min(ans, dot);
            }
            
            if (S[h][w-K+1] == 'o')
            {
                circle -= 1;
            } else if (S[h][w-K+1] == '.')
            {
                dot -= 1;
            }
        }
    }

    for (int w = 0; w < W; w++)
    {
        int circle = 0, dot = 0;
        for (int h = 0; h < min(H,K-1); h++)
        {
            if (S[h][w] == 'o')
            {
                circle += 1;
            } else if (S[h][w] == '.')
            {
                dot += 1;
            }
        }
        for (int h = K-1; h < H; h++)
        {
            if (S[h][w] == 'o')
            {
                circle += 1;
            } else if (S[h][w] == '.')
            {
                dot += 1;
            }

            if (circle + dot == K)
            {
                ans = min(ans, dot);
            }
            
            if (S[h-K+1][w] == 'o')
            {
                circle -= 1;
            } else if (S[h-K+1][w] == '.')
            {
                dot -= 1;
            }
        }
    }

    if (ans == K+1)
    {
        cout << -1;
    } else
    {
        cout << ans;
    }
}