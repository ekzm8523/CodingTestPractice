//
////
//// Created by Macbook Pro on 2021/01/04.
////
//
//#include <iostream>
//#include <vector>
//#include <queue>
//
//#define INF 1e9
//using namespace std;
//
//int n,m,start;
//
//void dijkstra(vector<pair<int,int>> v[], int d[], int start){
//    priority_queue<pair<int,int>> pq;
//
//    pq.push({0,start});
//    d[start] = 0;
//
//    while(!pq.empty()){
//        int dis = -pq.top().first;
//        int now = pq.top().second;
//        pq.pop();
//
//        if(d[now] < dis) continue;
//
//        for(int i=0;i<v[now].size();i++){
//            int cost = dis + v[now][i].second;
//            if(cost < d[v[now][i].first]){
//                d[v[now][i].first] = cost;
//                pq.push(make_pair(-cost,v[now][i].first));
//            }
//        }
//    }
//}
//
//int main(){
//
//
//    cin >> n >> m >> start;
//
//    vector<pair<int,int>> v[n+1];
//    int d[n+1];
//
//    for(int i=0;i<m;i++){
//        int a,b,c;
//        cin >> a >> b >> c;
//        v[a].push_back({b,c});
//    }
//
//    fill(d+1,d+n+1,INF);
//
//    dijkstra(v,d,start);
//
//    for(int i=1;i<=n;i++){
//        cout << " d " << i << " : " << d[i] << endl;
//        for(int j=0;j<v[i].size();j++){
//            cout << i << " : " << v[i][j].first << "  " << v[i][j].second << endl;
//        }
//        cout << endl;
//    }
//    int cnt = 0;
//    int time = 0;
//    for(int i=1;i<=n;i++){
//        if(d[i] != INF && d[i] != 0){
//            cnt++;
//            time = time < d[i]?d[i]:time;
//        }
//
//    }
//    cout << "cnt == " << cnt << endl;
//    cout << "time == " << time << endl;
//    return 0;
//}
