////
//// Created by Macbook Pro on 2020/11/12.
//// 위의 Solution은 우선순위 큐를 몰랐을 때이고 아래의 Solution은 우선순위 큐를 배워 적용시킨 코드이다.
////
//
//#include <stack>
//#include <vector>
//#include <iostream>
//#include <algorithm>
//#include <queue>
//
//using namespace std;
////
////int mixScoville(int first,int second){
////    return first + second*2;
////}
////int solution(vector<int> scoville, int K) {
////    vector<int>::iterator it = scoville.begin();
////    stack<int> scovilleStack;
////    int mixAfter=0;
////    int answer = 0;
////    sort(scoville.begin(),scoville.end());
////    for(int i=0;i<scoville.size();i++)
////        scovilleStack.push(scoville[scoville.size()-1-i]);
////
////    while(scovilleStack.top() < K){ // 섞은 후
////
////        mixAfter = mixScoville(scoville[0],scoville[1]);
////        if(scoville.size()<2 && mixAfter <K) return -1;
////        scoville.erase(scoville.begin());
////        scoville.erase(scoville.begin());
////
////        scoville.push_back(mixAfter);
////        sort(scoville.begin(),scoville.end());
////
////        answer++;
////    }
////    return answer;
////}
//int solution(vector<int> scoville, int K){
//    int answer = 0;
//    int first,second;
//
//    priority_queue<int, vector<int>, greater<int>> scovilleQueue(scoville.begin(), scoville.end());
//
//    while(scovilleQueue.top() < K){
//        if(scovilleQueue.size() == 1) return -1;
//        first = scovilleQueue.top();
//        scovilleQueue.pop();
//        second = scovilleQueue.top();
//        scovilleQueue.pop();
//        scovilleQueue.push(first + second*2);
//        answer++;
//
//    }
//    return answer;
//}
//
//int main (){
//    vector<int> scoville ={1,2,3,9,10,12};
//    int K = 7;
//
//    cout<< solution(scoville,K) << endl;
//    return 0;
//}