//#include <string>
//#include <vector>
//#include <queue>
//#include <iostream>
//#include <unordered_map>
//using namespace std;
//
//int solution(int bridge_length, int weight, vector<int> truck_weights) {
//    int answer=0,bridge_weight=0;
//
//    queue<int> cross_q;
//    int i=0;
//    while(truck_weights.size() > i){
//        answer++;
//        if(cross_q.size() == bridge_length){
//            bridge_weight -= cross_q.front();
//            cross_q.pop();
//        }
//        if(bridge_weight + truck_weights[i] <= weight){
//            bridge_weight += truck_weights[i];
//            cross_q.push(truck_weights[i]);
//            i++;
//        } else
//            cross_q.push(0);
//    }
//    answer += bridge_length;
//
//    return answer;
//
//}
//
//int main(){
//    int bridge_length = 2;
//    int weight = 10;
//    int answer;
//    vector<int> truck_weights = {7,4,5,6};
//    answer = solution(bridge_length,weight,truck_weights);
//    cout << answer;
//}
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
///*
// * int answer = 0;
//    int i=0;
//    int bridge_weight=0;
//    queue<int> bridge_queue;
//    while(truck_weights.size()>i){
//        answer++;
//        if(bridge_queue.size() == bridge_length){
//            bridge_weight -= bridge_queue.front();
//            bridge_queue.pop();
//        }
//        if(bridge_weight + truck_weights[i] <= weight){
//            bridge_weight += truck_weights[i];
//            bridge_queue.push(truck_weights[i]);
//            i++;
//        }
//        else
//            bridge_queue.push(0);
//    }
//    answer += bridge_length;
//
//    return answer;
// */