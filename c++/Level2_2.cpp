//////
////// Created by Macbook Pro on 2020/12/21.
//////
////
////#include <string>
////#include <vector>
////
////#include <iostream>
////using namespace std;
////
////int solution(string skill, vector<string> skill_trees) {
////    int answer = 0;
////    skill.find('A');
////    return answer;
////}
////int main(){
////    string skill = "ABC";
////
////    cout <<skill.find('B');
////}
////
//
//
//#include <string>
//#include <vector>
//#include <iostream>
//#include <map>
//#include <cstring>
//using namespace std;
//int cal(int a,int b,char op){
//    if(op == '+') return a + b;
//    if(op == '-') return a - b;
//    if(op == '*') return a * b;
//    if(op == '/') return a / b;
//}
//int opop(vector<int> numList, vector<char> opList, vector<char> op){
//
//    vector<char>::iterator opIt=opList.begin();
//    vector<int>::iterator numIt=numList.begin();
//    int size = opList.size();
//    for(int i=0;i<op.size();i++){
//        for(int j=0;j<size;j++){
//            if(opList[j] == op[i]){
//                int tmp = cal(numList[j],numList[j+1],op[i]);
//                numList.erase(numIt+j);
//                numList.erase(numIt+j+1);
//                opList.erase(opIt+j);
//                numList.insert(numIt+j,tmp);
//                size--;
//            }
//        }
//    }
//    return numIt[0];
//}
//
//long long solution(string expression) {
//    long long answer = 0;
//    int startIndex=0;
//    vector<int> numList;
//    vector<char> opList;
//    vector<char> op = {'+','-','*','/'};
//    for(int i=0;i<expression.size();i++){
//        if(expression[i] == '+' || expression[i] == '-' ||expression[i] == '*' ||expression[i] == '/'){
//            numList.push_back(stoi(expression.substr(startIndex,i-startIndex)));
//            opList.push_back(expression[i]);
//            startIndex = i+1;
//        }
//    }
//    numList.push_back(stoi(expression.substr(startIndex,expression.size()-startIndex)));
//
//    for(auto it : numList)
//        cout << it << endl;
//    for(auto it : opList)
//        cout << it << endl;
//    do{
//        cout << opop(numList,opList, op) << endl;
//
//    }while(next_permutation(op.begin(),op.end()));
//
//    return answer;
//}
//
//
//int main(){
//    string expresstion = "100-200*300-500+20";
//    cout << solution(expresstion);
//}