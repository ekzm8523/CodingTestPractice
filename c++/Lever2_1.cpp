//#include <iostream>
//#include<vector>
//using namespace std;
//
//#include <iostream>
//#include<vector>
//using namespace std;
//int answer=1234;
//bool isRect(vector<vector<int>> board, int x,int y, int n){
//
//    for(int i=x;i<x+n;i++){
//        for(int j=y;j<y+n;j++) {
//            if (board[i][j] == 0) return false;
//        }
//    }
//    return true;
//}
//int solution(vector<vector<int>> board)
//{
//    for(int i=0;i<board.size();i++){
//        for(int j=0;j<board[i].size();j++){
//            cout << board[i][j] << " ";
//        }
//        cout << endl;
//    }
//    for(int i=0;i<board.size();i++){
//        for(int j=0;j<board.size()-i;j++){
//            for(int k=0;k<board[j].size()-i;k++){
//                if(isRect(board,j,k,i+1)){
//                    answer = i+1;
//                    break;
//                }
//            }
//        }
//    }
//
//    return answer;
//}
//int main(){
//    vector<vector<int>> board = {{0,1,1,1},{0,1,1,1}};
//    cout << solution(board);
//
//}