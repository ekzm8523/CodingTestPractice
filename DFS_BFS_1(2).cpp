////
//// Created by Macbook Pro on 2020/12/05.
////
//
//#include <string>
//#include <vector>
//#include <iostream>
//
//using namespace std;
//int answer=0;
//int size=0;
//void dfs(vector<int> numbers, int depth,int sum,int target){
//    if(depth == size){
//        if(sum == target) answer++;
//        return;
//    }
//    dfs(numbers,depth+1,sum + numbers[depth],target);
//    dfs(numbers,depth+1,sum - numbers[depth],target);
//
//}
//
//int solution(vector<int> numbers, int target) {
//
//    size = numbers.size();
//    dfs(numbers,0,0,target);
//    return answer;
//}
//
//int main(){
//    int target=3;
//    vector<int> numbers = {1,1,1,1,1};
//
//    cout << solution(numbers,target);
//
//}