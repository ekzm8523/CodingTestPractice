//#include <iostream>
//#include <vector>
//#include <queue>
//using namespace std;
//
//int main() {
//
//    int N = 5, M = 7;
//    vector<vector<int>> v = {{1,2},{1,3},{1,4},{2,4},{3,4},{3,5},{4,5}};
//    int graph[N+1][N+1];
//    int K = 5, X = 4;
//
//
//
//    for( int i=1;i<=N;i++)
//        fill(graph[i]+1, graph[i]+N+1,9999);
//
//    for(int i=0;i<v.size();i++){
//        graph[v[i][0]][v[i][1]] = 1;
//        graph[v[i][1]][v[i][0]] = 1;
//    }
//    for(int i=1;i<=N;i++){
//        for(int j=1;j<=N;j++){
//            cout << graph[i][j] << " ";
//        }
//        cout << endl;
//    }
//    cout << "------------------"<<endl;
//    for(int k=1;k<=N;k++){
//        for(int i=1;i<=N;i++){
//            for(int j=1;j<=N;j++){
//                if(graph[i][k] + graph[k][j] < graph[i][j])
//                    graph[i][j] = graph[i][k] + graph[k][j];
//            }
//        }
//    }
//    for(int i=1;i<=N;i++){
//        for(int j=1;j<=N;j++){
//            cout << graph[i][j] << " ";
//        }
//        cout << endl;
//    }
//    cout << graph[1][K] + graph[K][X];
//
//    return 0;
//}