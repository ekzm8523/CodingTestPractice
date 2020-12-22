////
//// Created by Macbook Pro on 2020/12/21.
////
//#include <string>
//#include <vector>
//#include <iostream>
//#include <unordered_map>
//using namespace std;
//
//string solution(vector<string> participant, vector<string> completion) {
//    string answer = "";
//    unordered_map<string,int> m;
//    for(auto it:participant){
//        m[it]++;
//    }
//    for(auto it:completion){
//        //if(m[it] == 0) return it;
//        m[it]--;
//    }
//    for(auto it:m)
//        //cout << it.first << it.second << endl;
//        if(it.second) return it.first;
//}
//
//
//int main(){
//    vector<string> participant = {"leo","kiki","eden","kiki"};
//    vector<string> completion = {"eden","kiki","leo"};
//    cout << solution(participant,completion) << endl;
//}