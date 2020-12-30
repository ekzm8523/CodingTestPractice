//
// Created by Macbook Pro on 2020/12/30.
//

#include <iostream>
#include <vector>

using namespace std;
int n = 5;
int m = 6;
int answer = 999;
void bfs(vector<vector<int>> v,int i,int j,int moveCnt,vector<vector<bool>> check){


    if(i<0 || i>=n || j <0 || j>=m) return; // out of index
    if(check[i][j] == true || v[i][j] == 0) return;
    check[i][j] = true;
    if(i == n-1 && j == m-1 && moveCnt < answer) answer = moveCnt; // answer

    bfs(v,i+1,j,moveCnt+1,check);
    bfs(v,i-1,j,moveCnt+1,check);
    bfs(v,i,j+1,moveCnt+1,check);
    bfs(v,i,j-1,moveCnt+1,check);
}

int main(){

    vector<vector<int>> v = {{1,1,1,1,1,1},
                             {1,1,1,1,0,1},
                             {0,0,0,0,1,1},
                             {1,1,1,1,1,0},
                             {1,1,1,1,1,1}};
    vector<vector<bool>> check(n,vector<bool>(m));
    bfs(v,0,0,1,check);

    cout << answer;
    return 0;
}
