//
// Created by Macbook Pro on 2020/11/12.
//

#include <iostream>

using namespace std;

#include <string>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

struct cmp{
    bool operator()(vector<int> a, vector<int> b){
        return a.at(1)>b.at(1);
    }
};

int solution(vector<vector<int>> jobs) {
    int answer = 0,j=0,time=0;

    priority_queue<vector<int>,vector<vector<int>>,cmp> pq;
    sort(jobs.begin(),jobs.end());

    while(j<jobs.size() || !pq.empty()){
        if(j<jobs.size() && time >= jobs[j][0]){
            pq.push(jobs[j++]);
            continue;
        }
        if(!pq.empty()){
            time += pq.top()[1];
            answer += time-pq.top()[0];
            pq.pop();
        }
        else
            time = jobs[j][0];
    }



    return answer/jobs.size();
}

int main()
{
    vector<vector<int>> jobs = {{0,3},{1,9},{0,6}};
    cout<<solution(jobs)<<endl;

    return 0;
}