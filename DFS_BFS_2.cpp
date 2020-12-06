//
// Created by Macbook Pro on 2020/12/06.
//

#include <iostream>
#include <vector>
using namespace std;

void dfs(int n, vector<vector<int>>& computers){

    if(!computers[n][n]) return;
    computers[n][n] = 0;
    for(int i=0;i<computers.size();i++){
        if(computers[n][i] && computers[i][i]){
            dfs(i,computers);
        }
    }
}

int solution(int n, vector<vector<int>> computers) {
    int answer=0;

    for(int i=0;i<n;i++){
        if(!computers[i][i]) continue;
        answer++;
        dfs(i,computers);
    }

    return answer;
}
int main(){
    int n = 5;
    vector<vector<int>> computers = {{1,0,1,1,0},
                                     {0,1,0,1,0},
                                     {1,0,1,0,0},
                                     {1,1,0,1,1},
                                     {0,0,0,1,1}};
    cout << solution(n,computers) << endl;
}