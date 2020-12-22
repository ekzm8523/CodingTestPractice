//#include <string>
//#include <vector>
//#include <iostream>
//#include <algorithm>
//using namespace std;
//
//vector<int> solution(vector<int> answers) {
//    vector<int> answer;
//    int size = answers.size();
//    answer.resize(size,0);
//    vector<int> st1 = {1,2,3,4,5};
//    vector<int> st2 = {2,1,2,3,2,4,2,5};
//    vector<int> st3 = {3,3,1,1,2,2,4,4,5,5};
//    int i=0;
//
//    for(auto it : answers){
//        if(st1[i % st1.size()] == it) answer[0]++;
//        if(st2[i % st2.size()] == it) answer[1]++;
//        if(st3[i % st3.size()] == it) answer[2]++;
//        i++;
//    }
//    int max = *max_element(answer.begin(),answer.end());
//    vector<int> tmp;
//    for(int i=0;i<3;i++)
//        if(answer[i] == max)
//            tmp.push_back(i+1);
//
//    return tmp;
//}
//
//int main(){
//
////    vector<int> answers ={1,2,3,4,5};
//    vector<int> answers ={1,3,2,4,2};
//
//    answers = solution(answers);
//    for(auto it:answers)
//        cout << it << " ";
//    cout << endl;
//
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
//
//
//
//
//
//
//
