////
//// Created by Macbook Pro on 2020/12/18.
////
//
//#include <string>
//#include <vector>
//#include <iostream>
//
//using namespace std;
//
//int solution(int n, vector<vector<int>> results) {
//    int answer = 0;
//
//    vector<vector<int>> graph(n,vector<int>(n,0));
//
//    for(int i=0;i<results.size();i++)
//        graph[results[i][0]-1][results[i][1]-1] = 1;
//
//
//    cout << endl;
//    for(int k=0;k<n;k++){
//        for(int i=0;i<n;i++){
//            for(int j=0;j<n;j++){
//                if(!graph[i][j] && graph[i][k] && graph[k][j]){
//                    cout << i << " " << k << " " << j << endl;
//                    graph[i][j] =1;
//                }
//            }
//        }
//    }
//
//
//    for(int i=0;i<n;i++){
//        for(int j=0;j<n;j++){
//            if((graph[i][j] || graph[j][i]) && i != j){
//                graph[i][i]++;
//            }
//        }
//        if(graph[i][i] == n-1) answer++;
//    }
//
//    return answer;
//}
//int main(){
//
//    vector<vector<int>> result = {{4,3},{4,2},{3,2},{1,2},{2,5}};
//    int n = 5;
//    cout << solution(n,result);
//    return 0;
//}