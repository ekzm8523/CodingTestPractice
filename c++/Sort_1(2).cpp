////
//// Created by Macbook Pro on 2020/11/13.
////
//
//#include <string>
//#include <vector>
//#include <iostream>
//#include <algorithm>
//using namespace std;
//
//vector<int> solution(vector<int> array, vector<vector<int>> commands) {
//    vector<int> answer;
//
//    for(int n=0;n<commands.size();n++){
//        vector<int> tmp(&array[commands[n][0]-1],&array[commands[n][1]]);
//        sort(tmp.begin(),tmp.end());
//        answer.push_back(tmp[commands[n][2]-1]);
//    }
//    return answer;
//}
//
//int main(){
//    vector<int> array = {1,5,2,6,3,7,4};
//    vector<vector<int>> commands = {{2,5,3},{4,4,1},{1,7,3}};
//    vector<int> answer = solution(array,commands);
//
//    for(auto it:answer)
//        cout << it << " ";
//    cout << endl;
//    return 0;
//}
//
