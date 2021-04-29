////
//// Created by Macbook Pro on 2020/12/18.
////
//
//#include <iostream>
//#include <string>
//#include <vector>
//#include <queue>
//using namespace std;
//int maxDepth = 0;
//int bfs(int n,vector<vector<int>> AdjacencyMatrix){
//    queue<int> q;
//    int start=1,depth = 1;
//    vector<bool> check(n+1,false);
//    vector<int> depthArray(n+1,0);
//    q.push(start);
//    check[start] = true;
//    depthArray[start] = 1;
//    int cnt=0;
//    while(!q.empty()){
//        int tmp = q.front();
//        cnt++;
//        q.pop();
//        for(int i=0;i<AdjacencyMatrix[tmp].size();i++){
//            if(!check[AdjacencyMatrix[tmp][i]]) {
//                check[AdjacencyMatrix[tmp][i]] = true;
//                depthArray[depth+1]++;
//                q.push(AdjacencyMatrix[tmp][i]);
//            }
//        }
//        if(cnt == depthArray[depth]){
//            cnt = 0;
//            depth++;
//        }
//    }
//    return depthArray[depth-1];
//
//}
//
//int solution(int n, vector<vector<int>> edge) {
//
//    vector<vector<int>> AdjacencyList(n+1,vector<int>());
//    for(int i=0;i<edge.size();i++){
//        AdjacencyList[edge[i][0]].push_back(edge[i][1]);
//        AdjacencyList[edge[i][1]].push_back(edge[i][0]);
//    }
//    return bfs(n,AdjacencyList);
//}
//
//int main(){
//
//    vector<vector<int>> edge = {{3,6},{4,3},{3,2},{1,3},{1,2},{2,4},{5,2}};
//    int n = 6;
//    cout << solution(n,edge);
//
//
//    return 0;
//}
