//#include <string>
//#include <vector>
//#include <stack>
//#include <iostream>
//using namespace std;
//
//vector<int> solution(vector<int> progresses, vector<int> speeds) {
//    vector<int> answer;
//    stack<int> Stack;
//    stack<int> speedStack;
//    int time = 0;
//    int cnt = 0;
//
//    for(int i=progresses.size()-1; i>=0; i--) {
//        Stack.push(progresses[i]);
//        speedStack.push(speeds[i]);
//    }
//
//    while(Stack.size()>0){
//        cnt=0;
//        while(Stack.top()+(time*speedStack.top())<100) time++;
//        while(Stack.top()+(time*speedStack.top())>=100 && Stack.size()>0){
//            Stack.pop();
//            speedStack.pop();
//            cnt++;
//            if(Stack.size()<=0)break;
//        }
//        answer.push_back(cnt);
//    }
//
//    return answer;
//}
//
//int main(){
//    vector<int> progresses = {95,90,99,99,80,99};
//    vector<int> speeds = {1,1,1,1,1,1};
//    vector<int> answer;
//
//    answer = solution(progresses,speeds);
//
//    for(auto it:answer) cout << it << endl;
//
//
//}