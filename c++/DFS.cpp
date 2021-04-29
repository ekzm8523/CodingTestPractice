////
//// Created by Macbook Pro on 2020/12/05.
////
//
//#include <iostream>
//#include <stdio.h>
//#include <vector>
//#include <algorithm>
//using namespace std;
//
//void dfs(int start, vector<int> graph[], bool check[]){
//
//    check[start] = true;
//    printf("%d ",start);
//    for(int i=0;i<graph[start].size();i++){
//        int next = graph[start][i];
//        if(check[next] == false){
//            dfs(next,graph,check);
//        }
//    }
//}
//
//int main(){
//    int n,m,start;
//    cin >> n >> m >> start;
//
//    vector<int> graph[n+1];
//
//    bool check[n+1];
//    fill(check,check+n+1,false);
//    for(int i=0;i<m;i++){
//        int u,v;
//        cin >> u >> v;
//        graph[u].push_back(v);
//        graph[v].push_back(u);
//    }
//    for(int i=1;i<=n;i++){
//        sort(graph[i].begin(),graph[i].end());
//    }
//    dfs(start,graph,check);
//
//    return 0;
//}
//
//
////
////#include <string>
////#include <vector>
////#include <unordered_map>
////#include <queue>
////#include <iostream>
////
////using namespace std;
////class Graph;
////
////
////
////
////class Graph {
////private:
////    enum { NON_CONNECT = 0, CONNECT = 1 };
////    vector <vector<int>> adjacencyMatrix;
////    int vertexCount;
////    vector<bool> isvisited;
////    unordered_map<int, string> idxToKeyMap;
////    unordered_map<string, int> keyToidxMap;
////
////    int generateIdxForKey = 0;
////    int generateIdx() {
////        int cur = generateIdxForKey;
////        generateIdxForKey++;
////        return cur;
////    }
////
////    void insertVertexToMaps(const string& vertex) {
////        if (keyToidxMap.find(vertex) == keyToidxMap.end()) {
////            int idx = generateIdx();
////            keyToidxMap[vertex] = idx;
////            idxToKeyMap[idx] = vertex;
////        }
////    }
////
////    class Payload {
////    public:
////        int level;
////        Payload(int level) {
////            this->level = level;
////        }
////    };
////
////    void BFS(int startVtxId, int startLevel) {
////        queue<int> bfsQueue;
////        queue<Payload> payloadQueue;
////        bfsQueue.push(startVtxId);
////        payloadQueue.push(Payload(startLevel));
////        isvisited[startVtxId] = true;
////        DoVisited(startVtxId, startLevel);
////        while (!bfsQueue.empty()) {
////
////            int vertexId = bfsQueue.front(); Payload payload = payloadQueue.front();
////            bfsQueue.pop(); payloadQueue.pop();
////            auto adjacents = GetAdjacents(vertexId);
////
////            for (auto adjacentVtxId : adjacents) {
////                if (!isvisited[adjacentVtxId]) {
////                    isvisited[adjacentVtxId] = true;
////                    DoVisited(adjacentVtxId, payload.level + 1);
////                    bfsQueue.push(adjacentVtxId);
////                    payloadQueue.push(Payload(payload.level + 1));
////                }
////            }
////
////        }
////    }
////
////
////    void DFS(int vertexId, int level) {
////        isvisited[vertexId] = true;
////        DoVisited(vertexId, level);
////        auto adjacents = GetAdjacents(vertexId);
////        for (auto adjacentVtxId : adjacents) {
////            if (!isvisited[adjacentVtxId]) {
////                DFS(adjacentVtxId, level + 1);
////            }
////        }
////
////    }
////    //컴파일러최적화 복사반환X (int , vector<int>& dest)와같음
////    vector<int> GetAdjacents(int vertexId) {
////        vector<int> adjacents;
////        for (int i = 0; i < vertexCount; i++) {
////            if (adjacencyMatrix[vertexId][i] == CONNECT) {
////                adjacents.push_back(i);
////            }
////        }
////        return adjacents;
////    }
////
////    void InitVisited() {
////        std::fill(isvisited.begin(), isvisited.end(), false);
////    }
////
////    void DoVisited(int vertexId, int level) {
////        cout << "visited" << vertexId << endl;
////        if (vertexId == endIdx) {
////            if (minimulPath > level) {
////                minimulPath = level;
////            }
////        }
////    }
////
////public:
////    Graph(int vertexCount) {
////        adjacencyMatrix = vector<vector<int>>(vertexCount, vector<int>(vertexCount));
////        isvisited = vector<bool>(vertexCount);
////        this->vertexCount = vertexCount;
////    }
////
////    void insertEdge(string vertexId1, string vertexId2) {
////        int vertexIdx1, vertexIdx2;
////        vertexIdx1 = keyToidxMap[vertexId1];
////        vertexIdx2 = keyToidxMap[vertexId2];
////        adjacencyMatrix[vertexIdx1][vertexIdx2] = CONNECT;
////        adjacencyMatrix[vertexIdx2][vertexIdx1] = CONNECT;
////    }
////
////    void insertVertex(string vertexId) {
////        insertVertexToMaps(vertexId);
////    }
////
////
////    void SolveBFS() {
////        InitVisited();
////        for (int vertexId = 0; vertexId < vertexCount; vertexId++) {
////            if (!isvisited[vertexId]) {
////                int level = 0;
////                BFS(vertexId, level);
////            }
////        }
////    }
////    void SolveDFS() {
////        InitVisited();
////        for (int vertexId = 0; vertexId < vertexCount; vertexId++) {
////            if (!isvisited[vertexId]) {
////                int level = 0;
////                DFS(vertexId, level);
////            }
////        }
////    }
////
////    int minimulPath = 999999999;
////    int endIdx;
////    void setEnd(const string& end) {
////        endIdx = -1;
////        if (keyToidxMap.find(end)!=keyToidxMap.end()) {
////            this->endIdx = keyToidxMap[end];
////        }
////    }
////    void SolveBFS2(const string& begin) {
////        InitVisited();
////        BFS(keyToidxMap[begin], 0);
////    }
////
////    bool isContainVertex(const string& a) {
////        if (keyToidxMap.find(a) != keyToidxMap.end()) {
////            return true;
////        }
////        return false;
////    }
////};
////
////
////bool isConnected(const string & a, const string & b) {
////    int difCount = 0;//몇개다른지체크
////    for (int i = 0; i < a.size(); i++) {
////        char c=a[i] - b[i];
////        if (c != 0) {
////            difCount++;
////            if (difCount > 1)
////                return false;
////        }
////
////    }
////    return true;
////}
////
////
////
////int solution(string begin, string target, vector<string> words) {
////    words.push_back(begin);
////    Graph graph(words.size());
////    for (const auto& word:words) {
////        graph.insertVertex(word);
////    }
////    for (int i = 0; i < words.size();i++) {
////        for (int j = i+1; j < words.size(); j++) {
////            if (isConnected(words[i], words[j])) {
////                graph.insertEdge(words[i], words[j]);
////            }
////        }
////    }
////
////    graph.setEnd(target);
////    graph.SolveBFS2(begin);
////
////    int answer = 0;
////    if (graph.minimulPath != 999999999)
////        answer = graph.minimulPath;
////
////    return answer;
////}