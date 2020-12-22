////
//// Created by Macbook Pro on 2020/12/22.
////
//#include <string>
//#include <vector>
//#include <unordered_map>
//#include <iostream>
//
//using namespace std;
//int solution(vector<vector<string>> clothes) {
//    unordered_map<string,int> m;
//    int answer=1;
//    for(int i=0;i<clothes.size();i++){
//        m[clothes[i][1]]++;
//    }
//    for(auto it:m)
//        answer *= (it.second+1);
//
//    return answer-1;
//}
//int main(){
//
//    vector<vector<string>> clothes{{"yellow_hat", "headgear"}, {"blue_sunglasses", "eyewear"}, {"green_turban", "headgear"}};
//
//    cout << solution(clothes);
//
//    return 0;
//}
