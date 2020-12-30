////
//// Created by Macbook Pro on 2020/12/30.
////
//
//
//#include <iostream>
//#include <vector>
//
//using namespace std;
//int n = 4;
//int m = 5;
//void dfs(vector<vector<int>> &v, int i, int j){
//
//    if(i < 0 || i >= n || j < 0 || j >= m) return;
//    if(v[i][j] == 1) return;
//
//    v[i][j] = 1;
//
//    dfs(v,i-1,j);
//    dfs(v,i+1,j);
//    dfs(v,i,j+1);
//    dfs(v,i,j-1);
//
//}
//
//int main(){
//
//    vector<vector<int>> v = {{0,0,1,1,0},
//                             {0,0,1,0,1},
//                             {1,1,1,1,1},
//                             {0,0,1,0,0}};
//    int answer=0;
//    for(auto it : v) {
//        for (auto it2 : it)
//            cout << it2 << " ";
//        cout << endl;
//    }
//
//    for(int i=0;i<v.size();i++)
//        for (int j=0;j<v[i].size();j++)
//            if(v[i][j] == 0){
//                dfs(v,i,j);
//                answer++;
//            }
//    cout << answer;
//    return 0;
//}
