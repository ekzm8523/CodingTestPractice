////
//// Created by Macbook Pro on 2020/11/13.
////
//
//#include <string>
//#include <vector>
//#include <iostream>
//#include <queue>
//
//using namespace std;
//
//
//vector<int> solution(vector<string> operations) {
//    vector<int> answer{0,0};
//    priority_queue<int> pq;
//
//    char instruction;
//    char *cNum;
//    int num;
//    for(int i=0;i<operations.size();i++){
//        priority_queue<int> pq2;
//        instruction = operations[i][0];
//        cNum = &operations[i][2];
//        num = stoi(cNum);
//        cout << "instruction => " << instruction << " num => " << num << endl;
//        if(instruction == 'I') {
//            pq.push(num);
//            cout << "insert of " << num << " " << endl;
//            cout << "size of " << pq.size() << endl;
//        }
//        if(instruction == 'D' && num == 1) {
//            if(pq.size() == 0) continue;
//            cout << "pop of " << pq.top() << endl;
//            pq.pop();
//
//        }
//        if(instruction == 'D' && num == -1){
//            if(pq.size() == 0) continue;
//            int size = pq.size();
//            for(int i=0;i<size-1;i++){
//                pq2.push(pq.top());
//                pq.pop();
//            }
//            cout << "pop of " << pq.top() << endl;
//            pq = pq2;
//            cout << "size of " << pq.size() << endl;
//        }
//    }
//    if(pq.size() > 0){
//
//        answer[0] = pq.top();
//        int size = pq.size();
//        for(int i=0;i<size-1;i++) {
//            cout << "erase of " << pq.top() << " " << endl;
//            pq.pop();
//
//        }
//        answer[1] = pq.top();
//
//    }
//    return answer;
//}
//
//int main(){
//
//    vector<string> operation = {"I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"};
//
////    vector<string> operation = {"I 16", "D 1"};
//    vector<int> sol = solution(operation);
//    cout <<  sol[0] << "   " << sol[1] << endl;
//
//
//
//    return 0;
//}