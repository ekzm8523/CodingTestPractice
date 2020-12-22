////
//// Created by Macbook Pro on 2020/12/21.
////
//#include <string>
//#include <vector>
//#include <iostream>
//#include <algorithm>
//using namespace std;
//vector<int> allData;
//bool check(int a){
//    if (a < 2 ) return false;
//    for(int i=2;i<a;i++)
//        if(a % i == 0) return false;
//    return true;
//}
//
//int solution(string numbers) {
//    vector<int> v;
//    int answer =0;
//    vector<int> ans;
//    for(auto it:numbers)
//        v.push_back(it-'0');
//    sort(v.begin(),v.end());
//
//    do{
//        for(int i=1;i<=v.size();i++){
//            int tmp = 0;
//            for(int j=0;j<i;j++){
//                tmp = (tmp * 10) + v[j];
//                ans.push_back(tmp);
//            }
//        }
//    }while(next_permutation(v.begin(),v.end()));
//
//
//    sort(ans.begin(),ans.end());
//    //ans.erase(unique(ans.begin(),ans.end()),ans.end());
//    for(auto it:ans){
//        cout << it << endl;
//        if(check(it)){
//            cout << "이건 소수다 " << it << endl;
//            answer++;
//        }
//    }
//    return answer;
//}
//int main(){
//
////    string numbers="17";
//    string numbers="011";
//
//    cout << solution(numbers) << endl;
//
//
//    return 0;
//}
