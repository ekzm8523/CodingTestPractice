//////
////// Created by Macbook Pro on 2020/12/14.
//////
////
////#include <iostream>
////#include <vector>
////#include <string>
////#include <algorithm>
////#include <stack>
////using namespace std;
////
////int main(){
////    vector<vector<string>> tickets = {{"ICN", "SFO"}, {"ICN", "ATL"}, {"SFO", "ATL"}, {"ATL","SFO"},{"ATL", "ICN"}, };
////    stack<int> st;
////    //st.push(1);
////    cout <<st.empty();
////    for(auto it:tickets){
////        cout << '['<< "'" << it[0] <<"', " << "'" << it[1] << "']";
////    }
////    cout << endl;
////
////    sort(tickets.begin(),tickets.end());
////
////    for(auto it:tickets){
////        cout << '['<< "'" << it[0] <<"', " << "'" << it[1] << "']";
////    }
////
////
////
////}
//
//#include <iostream>
//#include <vector>
//using namespace std;
//
//vector<int> solution(vector<vector<int> > v) {
//    vector<int> ans;
//
//    int x=0,y=0;
//    for(int i=0;i<3;i++){
//        x ^= v[i][0];
//        y ^= v[i][1];
//    }
//    ans.push_back(x);
//    ans.push_back(y);
//
//    return ans;
//}
//int main(){
//    vector<vector<int>> v = {{1,4},{3,4},{3,10}};
//    vector<int> ans = solution(v);
//    cout << ans[0] << " " << ans[1] << endl;
//    return 0;
//}