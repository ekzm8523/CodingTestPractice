//
// Created by Macbook Pro on 2020/12/05.
//

#include <string>
#include <vector>
#include <iostream>

using namespace std;
int size;
int answer=0;

void dfs(vector<int> graph,int target, int depth,int sum){

    if(depth == size){
        if(target == sum){
            answer++;
        }
        return;
    }
    dfs(graph,target, depth+1, sum+graph[depth]);
    dfs(graph,target, depth+1, sum-graph[depth]);

}

int solution(vector<int> numbers, int target) {

    size = numbers.size();

    dfs(numbers,target,0,0);

    return answer;
}
int main(){

    vector<int> numbers = {1,1,1,1,1};
    int target = 3;
    cout << solution(numbers,target);

}