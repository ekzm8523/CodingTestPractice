////
//// Created by Macbook Pro on 2021/01/02.
////
//
//#include <iostream>
//#include <vector>
//#include <algorithm>
//using namespace std;
//int max(int a,int b,int c){
//    int tmp = a>b?a:b;
//
//    return tmp>c?tmp:c;
//}
//int max(int a,int b){
//    return a>b?a:b;
//}
//
//
//int main(){
//
//    vector<vector<int>> v = {{1,3,3,2},{2,1,4,1},{0,6,4,7}};
//    int n = 4, m = 4;
//
////    vector<vector<int>> v = {{1,3,1,5},{2,2,4,1},{5,0,2,3},{0,6,1,2}}; // n * m
//
//    for(int i=1;i<v[0].size();i++){
//        for(int j=0;j<v.size();j++){
//            if(j-1 < 0)
//                v[j][i] += max(v[j][i-1],v[j+1][i-1]);
//            else if(j+1>=v.size())
//                v[j][i] += max(v[j-1][i-1],v[j][i-1]);
//            else
//                v[j][i] += max(v[j-1][i-1],v[j][i-1],v[j+1][i-1]);
//        }
//    }
//
//    for(int i=0;i<v.size();i++){
//        for(int j=0;j<v[i].size();j++){
//            cout << v[i][j] << " ";
//        }
//        cout << endl;
//    }
//
//
//    return 0;
//}