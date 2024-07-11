// LUOGU_RID: 157022645
#include<bits/stdc++.h>
#define int long long
#define endl '\n'
typedef long long ll;
using namespace std;
const int N = 105;
int a[5][5],tmp[5][5];
int check(){
	if(tmp[1][1] == tmp[1][2] && tmp[1][2] == tmp[1][3] && tmp[1][1])return tmp[1][3];
	if(tmp[2][1] == tmp[2][2] && tmp[2][2] == tmp[2][3] && tmp[2][1])return tmp[2][3];
	if(tmp[3][1] == tmp[3][2] && tmp[3][2] == tmp[3][3] && tmp[3][1])return tmp[3][3];
	if(tmp[1][1] == tmp[2][1] && tmp[2][1] == tmp[3][1] && tmp[1][1])return tmp[3][1];
	if(tmp[1][2] == tmp[2][2] && tmp[2][2] == tmp[3][2] && tmp[1][2])return tmp[1][2];
	if(tmp[1][3] == tmp[2][3] && tmp[2][3] == tmp[3][3] && tmp[1][3])return tmp[1][3];
	if(tmp[1][1] == tmp[2][2] && tmp[2][2] == tmp[3][3] && tmp[1][1])return tmp[1][1];
	if(tmp[1][3] == tmp[2][2] && tmp[2][2] == tmp[3][1] && tmp[1][3])return tmp[1][3];
	return 0;
}
int dfs(int dep){
	if(check()){
		return check();
	}
	if(dep == 10){
		int s1 = 0,s2 = 0;
		for(int i = 1;i <= 3;i++){
			for(int j = 1;j <= 3;j++){
				s1 += (tmp[i][j] == 1) * a[i][j];
				s2 += (tmp[i][j] == 2) * a[i][j];
			}
		}
		if(s1 > s2)return 1;
		else return 2;
	}
	bool flag1,flag2;
	if(dep & 1)flag1 = false,flag2 = true;
	else flag1 = true,flag2 = false;
	for(int i = 1;i <= 3;i++){
		for(int j = 1;j <= 3;j++){
			if(!tmp[i][j]){
				tmp[i][j] = (dep & 1 ? 1 : 2);
				if(dep & 1){
					int t = dfs(dep + 1);
					flag1 |= (t == 1);
					flag2 &= (t == 2);
				}else{
					int t = dfs(dep + 1);
					flag1 &= (t == 1);
					flag2 |= (t == 2);
				}
				tmp[i][j] = 0;
			}
		}
	}
//	cout << dep << " " << flag1 << " " << flag2 << endl;
	return (flag1 ? 1 : 2);
}
signed main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	for(int i = 1;i <= 3;i++){
		for(int j = 1;j <= 3;j++){
			cin >> a[i][j];
		}
	}
	cout << (dfs(1) == 1 ? "Takahashi" : "Aoki");
}
