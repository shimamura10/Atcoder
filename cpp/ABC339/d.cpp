#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;


int main(){
    int N;
    cin >> N;
    vector<string> S;
    for (size_t i = 0; i < N; i++)
    {
        string s;
        cin >> s;
        S.emplace_back(s);
    }
    vector<int> playerPos(4);
    bool trigger = false;
    for (size_t i = 0; i < N; i++)
    {
        for (size_t j = 0; j < N; j++)
        {
            if (S[i][j] == 'P')
            {
                if (!trigger)
                {
                    playerPos[0] = i;
                    playerPos[1] = j;
                    trigger = true;
                } else
                {
                    playerPos[2] = i;
                    playerPos[3] = j;
                }
            }
        }
    }
    int N2 = N*N;
    vector<vector<int>> minCosts(N2, vector<int>(N2, N2));
    minCosts[playerPos[0]*N + playerPos[1]][playerPos[2]*N + playerPos[3]] = 0;

    auto canGo = [&] (int x, int y) -> bool
    {
        if (x<0 || y<0 || x>=N || y>= N)
        {
            return false;
        }
        if (S[x][y] == '#')
        {
            return false;
        }
        return true;
    };

    // vector<vector<int>> minCosts(N^N, vector(N^N, N^N));
    queue<vector<int>> next;
    next.push(playerPos);
    int directions[4][2] = {{1,0}, {0,1}, {-1,0}, {0,-1}};
    while (!next.empty())
    {
        auto nowPos = next.front();
        for (auto direction : directions)
        {
            vector<int> nextPos(4,0);
            nextPos[0] = nowPos[0] + direction[0];
            nextPos[1] = nowPos[1] + direction[1];
            nextPos[2] = nowPos[2] + direction[0];
            nextPos[3] = nowPos[3] + direction[1];

            if (!canGo(nextPos[0], nextPos[1]))
            {
                nextPos[0] -= direction[0];
                nextPos[1] -= direction[1];
            }
            if (!canGo(nextPos[2], nextPos[3]))
            {
                nextPos[2] -= direction[0];
                nextPos[3] -= direction[1];
            }
            
            if (minCosts[nextPos[0]*N + nextPos[1]][nextPos[2]*N + nextPos[3]] == N2)
            {
                minCosts[nextPos[0]*N + nextPos[1]][nextPos[2]*N + nextPos[3]] = minCosts[nowPos[0]*N + nowPos[1]][nowPos[2]*N + nowPos[3]] + 1;
                next.push(nextPos);
            }
        }
        next.pop();
    }

    int ans = N2;
    for (int x = 0; x < N; x++)
    {
        for (int y = 0; y < N; y++)
        {
            ans = min(ans, minCosts[x*N+y][x*N+y]);
        }
    }
    if (ans == N2)
    {
        cout << -1;
    } else
    {
        cout << ans;
    }
}