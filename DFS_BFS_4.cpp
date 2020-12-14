//
// Created by Macbook Pro on 2020/12/12.
//


#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int max_cnt = 0;
void dfs(string start, vector<vector<string>> &tickets, vector<bool>& visit, vector<string>& answer, vector<string>& temp,int cnt){
    temp.push_back(start);
    if(max_cnt<cnt){
        max_cnt=cnt;
        answer=temp;
    }

    for(int i=0;i<tickets.size();i++){
        if(start == tickets[i][0] && !visit[i]){
            visit[i] = true;
            dfs(tickets[i][1],tickets,visit,answer,temp,cnt+1);
            visit[i] = false;
        }
    }
    temp.pop_back();
}

vector<string> solution(vector<vector<string>> tickets){
    int cnt = 0;
    vector<string> answer,temp;
    vector<bool> visit(tickets.size(),false);
    sort(tickets.begin(),tickets.end());
    dfs("ICN",tickets,visit,answer,temp,cnt);
    return answer;
}

int main(){
    //vector<vector<string>> tickets = {{"ICN", "SFO"}, {"ICN", "ATL"}, {"SFO", "ATL"}, {"ATL", "ICN"}, {"ATL","SFO"}};
    vector<vector<string>> tickets = {{"ICN", "JFK"}, {"HND", "IAD"}, {"JFK", "HND"}};
    vector<string> answer = solution(tickets);
    cout << '[';
    for(auto it:answer) cout << "'" << it <<"', ";
    cout << ']';
    return 0;
}

//
//void dfs(string start, vector<vector<string>> tickets, bool check[], vector<string>& answer){
//
//    if(answer.size() == tickets.size()+1) return;
//
//    for(int i=0;i<tickets.size();i++){
//        if(tickets[i][0] == start && !check[i] ){
//            answer.push_back(tickets[i][1]);
//            check[i] = true;
//            dfs(tickets[i][1],tickets,check,answer);
//            check[i] = false;
//        }
//    }
//
//}
//
//vector<string> solution(vector<vector<string>> tickets) {
//    vector<string> answer;
//    int i=0;
//    sort(tickets.begin(),tickets.end());
//    bool check [tickets.size()];
//    fill(check,check+tickets.size(),false);
//    string start = "ICN";
//    answer.push_back(start);
//    for(i=0;i<tickets.size();i++){
//        if(tickets[i][0] == start){
//            start = tickets[i][1];
//            answer.push_back(tickets[i][1]);
//            check[i] = true;
//            break;
//        }
//    }
//
//    dfs(start,tickets,check,answer);
//
//
//    return answer;
//}
