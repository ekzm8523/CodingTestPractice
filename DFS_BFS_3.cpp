//
// Created by Macbook Pro on 2020/12/07.
//


#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;
//void dfs(int start, vector<int> graph[], bool check[]){
//
//    check[start] = true;
//    printf("%d ",start);
//    for(int i=0;i<graph[start].size();i++){
//        int next = graph[start][i];
//        if(check[next] == false){
//            dfs(next,graph,check);
//        }
//    }
//}
//int solution(string begin, string target, vector<string> words) {
//    int answer = 0;
//    int cnt=0;
//    int len = words.size();
//    bool check[len+1];
//    fill(check,check+len,false);
//    vector<int> word_index [len];
//
//
//    for(int i=0;i<words.size();i++){
//        for(int j=0;j<words.size();j++){
//            if (i == j) continue;
//            cnt=0;
//            for(int z=0;z<words[j].size();z++)
//                if(words[j][z] == words[i][z]) cnt++;
//            if(cnt == words[i].size()-1){
//                word_index[i].push_back(j);
//            }
//        }
//    }
//
//    int start=0;
//    for(int i=0;i<words.size();i++){
//        cnt=0;
//        for(int j=0;j<begin.size();j++){
//            if(begin[j] == words[i][j]) cnt++;
//        }
//        if(cnt == words[i].size()-1){
//            start = i;
//        }
//    }
//
//    for(int i=0;i<len;i++) {
//        cout << words[i] << "  :  ";
//        for (int j=0;j<word_index[i].size();j++){
//            cout << words[word_index[i][j]] << " ";
//        }
//        cout << endl;
//    }
//
//    answer = dfs(start, word_index, check, target,words);
//
//    return answer;
//}


int answer=100;
bool checkDiff(string a, string b){
    int cnt = 0;
    for(int i=0;i<a.size();i++)
        if(a[i] == b[i]) cnt++;

    if(cnt == a.size()-1) return true;
    return false;

}
void dfs(string begin, string target, vector<string> words, bool check [], int depth){
    for(int i=0;i<words.size();i++){
        if(checkDiff(begin,words[i]) && !check[i]){
            if(words[i] == target) {
                answer = depth+1;
                return;
            }
            check[i] = true;
            dfs(words[i],target,words,check,depth+1);
            check[i] = false;
        }
    }
}


int solution(string begin, string target, vector<string> words){
    int tmp = 0;
    bool check [50] = {false};
    dfs(begin,target,words,check,0);
    if(answer == 100) return 0;
    return answer;

}


int main()
{
    vector<string> words = {"hot","dot","dog","lot","log","cog"};
    string begin = "hit";
    string target = "cog";
    cout << solution(begin,target,words);

    return 0;
}