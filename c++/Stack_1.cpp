//#include <string>
//#include <vector>
//#include <iostream>
//using namespace std;
//
//vector<int> solution(vector<int> prices) {
//    vector<int> answer;
//
//    for(int i=0;i<prices.size();i++){
//        int period = 0;
//        for(int j=i+1;j<prices.size();j++){
//            period++;
//            if(prices[i] > prices[j]){
//                break;
//            }
//        }
//        answer.push_back(period);
//    }
//    return answer;
//}
//
//int main(){
//    vector<int>prices = {1,2,3,2,3};
//    vector<int>answer;
//    answer = solution(prices);
//
//    for(auto it:answer) cout << it << " " << endl;
//
//    return 0;
//}