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
#include <numeric>
#include <set>
#include <random>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using vl = vector<long long>;
using vpii = vector<pair<int, int>>;

vpii cards;
// このcardsで先手が勝ちならtrue、負けならfalseを返す
bool dfs(vector<bool>& exist_cards) {
    // とれるカードを選出
    set<pair<int, int>> can_pick_cards;
    for (int i=0; i<cards.size()-1; i++) {
        if (!exist_cards[i]) { continue; }
        for (int j=i+1; j<cards.size(); j++) {
            if (!exist_cards[j]) { continue; }
            if (cards[i].first == cards[j].first || cards[i].second == cards[j].second) {
                can_pick_cards.insert(make_pair(i, j));
            }
        }
    }
    if (can_pick_cards.size() == 0) { return false; }
    for (auto& pick_card : can_pick_cards) {
        exist_cards[pick_card.first] = false;
        exist_cards[pick_card.second] = false;
        if (!dfs(exist_cards)) { 
            exist_cards[pick_card.first] = true;
            exist_cards[pick_card.second] = true;
            return true; 
            }
        exist_cards[pick_card.first] = true;
        exist_cards[pick_card.second] = true;
    }
    return false;
}

bool dfs(int exist_cards_bin, unordered_map<int, bool>& memo) {
    if (memo.count(exist_cards_bin) == 1) {
        return memo[exist_cards_bin];
    }
    // とれるカードを選出
    set<pair<int, int>> can_pick_cards;
    for (int i=0; i<cards.size()-1; i++) {
        if (!((exist_cards_bin >> i) & 1)) { continue; }
        for (int j=i+1; j<cards.size(); j++) {
            if (!((exist_cards_bin >> j) & 1)) { continue; }
            if (cards[i].first == cards[j].first || cards[i].second == cards[j].second) {
                can_pick_cards.insert(make_pair(i, j));
            }
        }
    }
    if (can_pick_cards.size() == 0) { return false; }
    for (auto& pick_card : can_pick_cards) {
        exist_cards_bin -= (1 << pick_card.first);
        exist_cards_bin -= (1 << pick_card.second);
        if (!dfs(exist_cards_bin, memo)) { 
            exist_cards_bin += (1 << pick_card.first);
            exist_cards_bin += (1 << pick_card.second);
            return memo[exist_cards_bin] = true;
        }
        exist_cards_bin += (1 << pick_card.first);
        exist_cards_bin += (1 << pick_card.second);
    }
    return memo[exist_cards_bin] = false;
}

int main(){
    int N;
    cin >> N;
    for (int i=0; i<N; i++) {
        int a, b;
        cin >> a >> b;
        cards.emplace_back(a,b);
    }
    vector<bool> exist_cards(N, true);
    int exist_cards_bin = (1 << N) - 1;
    unordered_map<int, bool> memo;
    if (dfs(exist_cards_bin, memo)) {
        cout << "Takahashi";
    } else {
        cout << "Aoki";
    }
}