#include <iostream>
#include <algorithm>
#include <vector>
#include <functional>
#include <unordered_map>
#include <memory>
#include <queue>
#include <unordered_set>
#include <limits>
#include <tuple>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using vl = vector<long long>;

int grid[3][3] = {{0,0,0}, {0,0,0}, {0,0,0}};

void print_grid() {
    for (int i=0; i<3; i++) {
        for (int j=0; j<3; j++) {
            cout << grid[i][j] << " ";
        }
        cout << endl;
    }
    cout << "----------------" << endl;
}


int check_agari(const ll point_grid[3][3]) {
    for (int i=0; i<3; i++) {
        // よこ
        if (grid[i][0] != 0 && grid[i][0] == grid[i][1] && grid[i][1] == grid[i][2]) {
            return grid[i][0];
        }
        // たて
        if (grid[0][i] != 0 && grid[0][i] == grid[1][i] && grid[1][i] == grid[2][i]) {
            return grid[0][i];
        }
    }
    // ななめ
    if (grid[1][1] != 0 && grid[0][0] == grid[1][1] && grid[1][1] == grid[2][2]) {
        return grid[1][1];
    }
    if (grid[1][1] != 0 && grid[2][0] == grid[1][1] && grid[1][1] == grid[0][2]) {
        return grid[1][1];
    }

    for (int i=0; i<3; i++) {
        for (int j=0; j<3; j++) {
            if (grid[i][j] == 0) {
                return 0;
            }
        }
    }
    
    ll point[2] = {0,0};
    for (int i=0; i<3; i++) {
        for (int j=0; j<3; j++) {
            if (grid[i][j] == 1) {
                point[0] += point_grid[i][j];
            } else {
                point[1] += point_grid[i][j];
            }
        }
    }
    // print_grid();
    if (point[0] > point[1]) {
        return 1;
    } else {
        return 2;
    }
}


bool can_win(int first, const ll point_grid[3][3]) {
    // print_grid();
    int second;
    if (first == 1) {
        second = 2;
    } else {
        second = 1;
    }
    auto tmp = check_agari(point_grid);
    if (tmp == first) {
        // print_grid(grid);
        return true;
    } else if (tmp == second){
        return false;
    }

    for (int i=0; i<3; i++) {
        for (int j=0; j<3; j++) {
            if (grid[i][j] == 0) {
                grid[i][j] = first;
                if (!can_win(second, point_grid)) {
                    grid[i][j] = 0;
                    return true;
                }
                grid[i][j] = 0;
            }
        }
    }
    return false;
}



int main(){
    ll point_grid[3][3];
    for (int i=0; i<3; i++) {
        for (int j=0; j<3; j++) {
            ll p;
            cin >> p;
            point_grid[i][j] = p;
        }
    }
    
    if (can_win(1, point_grid)) {
        cout << "Takahashi";
    } else {
        cout << "Aoki";
    }
    return 0;
}