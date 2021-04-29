////
//// Created by Macbook Pro on 2020/12/22.
////
//#include <iostream>
//#include <unordered_map>
//#include <string>
//#include <vector>
//using namespace std;
//
//int answer = -1;
//
//long long factorial(int n){
//    int x=1;
//    for(int i=2;i<=n;i++){
//        x *= i;
//    }
//    return x;
//}
//
//long long solution(int n){
//    long long answer = 0;
//
//
//
//    return answer;
//}
//
//
//
//int main(){
//    cout << solution (2);
//    return 0;
//}
//
//
//
////int solution(string s){
////    int answer = -1;
////    unordered_map<char,int> m;
////    for(int i=0;i<s.size();i++){
////        m[s[i]]++;
////    }
////    for(auto it : m)
////        cout << it.first << " " << it.second << endl;
////    return answer;
////}
//
////int solution(vector<int> arr){
////    int answer = 0;
////    int cnt=1;
////    while(!(arr.size() == 1 && arr[0] == 1)) {
////        answer++;
////
////        if(arr.size()==1)
////            break;
////        vector<int> tmp;
////        for (int i = 0; i < arr.size(); i++) {
////            if (i == arr.size() - 1) {
////                tmp.push_back(cnt);
////                cnt=1;
////                break;
////            }
////            if (arr[i] == arr[i + 1]) cnt++; // 같은거면 ++
////            else { // 다른거면 넣어준후 초기화
////                tmp.push_back(cnt);
////                cnt = 1;
////            }
////        }
////        arr = tmp;
////        for (auto it:arr)
////            cout << " " << it;
////        cout << endl;
////
////    }
////    return answer;
////}
////
////
////int solution(int N,vector<int> sequence){
////    int answer = 0;
////    int _size = sequence.size();
////
////    int p = sequence[0];
////    for(int i=1;i<_size;i++){
////        if(abs(sequence[i] - p) < abs(N - sequence[i] + p)) answer += abs(sequence[i]-p);
////        else answer += abs(N - sequence[i] + p);
////        p = sequence[i];
////        cout << sequence[i-1] << " move to" << p << endl;
////        cout << "cost of" << answer<<endl;
////    }
////
////    return answer;
////}
///*
// *
// * void dfs(vector<int> nums, int depth,int position, bool check []){
//
//    if(position >= nums.size() || position < 0) return; // 장외
//    if(position == nums.size()-1) { // 종료조건
//        if(answer < depth) answer = depth;
//        return;
//    }
//    check[position] = true;
//
//    if(!check[position + nums[position]] && nums[position + nums[position]] != 0)
//        dfs(nums,depth+1,position + nums[position],check);
//    if(!check[position - nums[position]] && nums[position - nums[position]] != 0)
//        dfs(nums,depth+1,position - nums[position],check);
//}
//int solution(vector<int> nums){
//    bool check [nums.size()];
//    fill(check,check+nums.size()-1,false);
//    dfs(nums,0,0,check);
//
//    return answer;
//}
// */