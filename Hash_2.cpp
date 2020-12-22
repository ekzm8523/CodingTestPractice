////
//// Created by Macbook Pro on 2020/12/21.
////
//
//#include <string>
//#include <vector>
//#include <algorithm>
//#include <iostream>
//
//using namespace std;
//
//bool solution(vector<string> phone_book) {
//    bool answer = true;
//    sort(phone_book.begin(),phone_book.end());
//
//    for(auto it : phone_book)
//        cout << it << " " << endl;
//
//    for(int i=0;i<phone_book.size()-1;i++){
//        if(phone_book[i+1].find(phone_book[i])==0) return false;
//    }
//
//    return answer;
//}
//
//int main(){
//    vector<string> phone_book = {"119", "97674223", "1195524421"};
//
//    cout << solution(phone_book) << endl;
//    return 0;
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
///*
//bool solution(vector<string> phone_book) {
//    bool answer = true;
//
//    sort(phone_book.begin(),phone_book.end());
//    for(int i=0;i<phone_book.size()-1;i++){
//        if(phone_book[i+1].find(phone_book[i]) == 0){
//            return false;
//        }
//    }
//    return answer;
//}
// */