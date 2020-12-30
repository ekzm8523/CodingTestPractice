////
//// Created by Macbook Pro on 2020/12/30.
////
//
//#include <iostream>
//#include <vector>
//#include <queue>
//
//using namespace std;
//int n = 5;
//int m = 6;
//int answer = 999;
//int dx[] = {0,1,0,-1};
//int dy[] = {-1,0,1,0};
//void bfs(vector<vector<int>> &v){
//    queue<pair<int,int>> q;
//    int x=0,y=0;
//
//    q.push({x,y});
//
//    while(!q.empty()){
//        x = q.front().first;
//        y = q.front().second;
//        q.pop();
//        for(int i=0;i<4;i++){ // 4방향
//            int nx = x + dx[i];
//            int ny = y + dy[i];
//            if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
//            if(v[nx][ny] == 0) continue;
//            if(v[nx][ny] == 1) {
//                v[nx][ny] = v[x][y] + 1;
//                q.push({nx,ny});
//            }
//        }
//    }
//}
//
//int main(){
//
//    vector<vector<int>> v = {{1,1,1,1,1,1},
//                             {1,1,1,1,0,1},
//                             {0,0,0,0,1,1},
//                             {1,1,1,1,1,0},
//                             {1,1,1,1,1,1}};
//    vector<vector<bool>> check(n,vector<bool>(m));
//    bfs(v);
//
//    for(int i=0;i<n;i++){
//        for(int j=0;j<m;j++){
//            cout << v[i][j] << " ";
//        }
//        cout <<endl;
//    }
//
//    return 0;
//}
