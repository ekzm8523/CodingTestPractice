////
//// Created by Macbook Pro on 2020/12/07.
////
//
//
//#include <iostream>
//#include <string>
//#include <vector>
//
//using namespace std;
//
//int answer=100;
//bool nodeConnect(string a, string b){
//    int diff=0;
//    for(int i=0;i<a.size();i++)
//        if(a[i] != b[i]) diff++;
//    if(diff == 1) return true;
//    return false;
//}
//
//void dfs(string begin, string target, vector<string> words, bool check[], int depth){
//    if(begin == target) {
//        answer = depth;
//        return;
//    }
//    if(depth == words.size()-1) return;
//
//    for(int i=0;i<words.size();i++){
//        if(!check[i] && nodeConnect(begin,words[i])){
//            check[i] = true;
//            dfs(words[i],target,words,check,depth+1);
//        }
//    }
//}
//
//
//int solution(string begin, string target, vector<string> words){
//    bool check[words.size()];
//    fill(check, check+words.size(),false);
//    dfs(begin,target,words,check,0);
//    if(answer == 100) return 0;
//    return answer;
//}
//
//int main()
//{
//    vector<string> words = {"hot","dot","dog","lot","log"};
//    string begin = "hit";
//    string target = "cog";
//    cout << solution(begin,target,words);
//
//    return 0;
//}