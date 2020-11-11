//#include <string>
//#include <vector>
//#include <unordered_map>
//#include <map>
//#include <iostream>
//#include <set>
//using namespace std;
//
//vector<int> solution(vector<string> genres, vector<int> plays) {
//    vector<int> answer;
//    unordered_map<string,int> hash;
//    map<int,string,greater<int>> hash2;
//    for (int i=0;i<genres.size();i++)
//        hash[genres[i]] += plays[i];
//
//    for (auto it:hash){
//        hash2[it.second] = it.first;
//    }
//    multimap<int,int,greater<int>> tmp_map;
//
//    for(auto it:hash2){
//        tmp_map.clear();
//        for(int i=0;i<genres.size();i++){
//            if(genres[i] == it.second){
//                tmp_map.insert(pair<int,int>(plays[i],i));
//                //cout<< "key :: " << plays[i] << " value :: " << i << endl;
//            }
//        }
//        int size=0;
//        for(auto it2:tmp_map) {
//            answer.push_back(it2.second);
//            size++;
//            if(size == 2) break;
//        }
//        tmp_map.empty();
//    }
//    for (auto it:answer) cout << it << "  " << endl;
//    return answer;
//}
//
//int main(){
//    vector<string> genres = {"classic", "pop", "classic", "classic", "pop"};
//    vector<int> plays = {2500,2500,2500,2500,2500};
//
//    solution(genres,plays);
//
//}