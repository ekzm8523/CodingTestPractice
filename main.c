/*
//
// 문제 3
//
*/
/*
#include <stdio.h>
#pragma warning(disable:4996)

typedef struct student {
    char name[10];
    int score;

}st;

int main() {
    st group[5];
    int sum=0;
    double avg;

    for(int i=0;i<5;i++){
        scanf("%s %d",group[i].name,&group[i].score);
        getchar();
        sum += group[i].score;
    }
    avg = (double)sum/5;

    for(int i=0;i<5;i++){
        if(avg>group[i].score)
            printf("%s\n",group[i].name);
    }

    return 0;
}*//*


//
// 문제 4
//
*/
/*
#include <stdio.h>

typedef struct strident{
    char name[20];
    int score[3];
    int sum;
    double avg;
    char grade;
}st;
int main()
{
    st std[20];
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        getchar();
        scanf("%s %d %d %d",std[i].name,&std[i].score[0],&std[i].score[1],&std[i].score[2]);
        std[i].sum += std[i].score[0] + std[i].score[1] + std[i].score[2];
        std[i].avg = (double)std[i].sum / 3;
        if(std[i].avg >= 90) std[i].grade = 'A';
        else if(std[i].avg >= 80) std[i].grade = 'B';
        else if(std[i].avg >= 70) std[i].grade = 'C';
        else std[i].grade = 'F';
    }
    for(int i=0;i<n;i++)
        printf("%s %.1f %c\n",std[i].name,std[i].avg,std[i].grade);

    return 0;
}
 *//*

//
//  문제 5
//
*/
/*
#include <stdio.h>

typedef struct student{
    char name[10];
    int score[3];
    int sum;
    double avg;
    char grade;
}st;

int main(){

    st std[50];
    st *p = std;

    int n;
    scanf("%d",&n);

    for(p = std;p != std+n;p++){
        getchar();
        scanf("%s %d %d %d",p->name,&p->score[0],&p->score[1],&p->score[2]);
        p->sum += p->score[0] + p->score[1] + p->score[2];
        p->avg = (double)p->sum / 3;
        if(p->avg >= 90) p->grade = 'A';
        else if(p->avg >= 80) p->grade = 'B';
        else if(p->avg >= 70) p->grade = 'C';
        else p->grade = 'D';
    }
    for(p = std;p != std+n;p++)
        printf("%s %.1f %c\n",p->name,p->avg,p->grade);

    return 0;
}
 *//*

*/
/*
 *
#include <stdio.h>

typedef struct student{
    int sex;
    int weight;
    int height;
    int grade;
}st;


int checkGrade(int sex,int weight,int height){
    if(sex == 1){ // 남자
        if( weight < 60 ){
            if(height < 165) return 1;
            else if(height < 175) return 2;
            else if(height >= 175) return 3;
        }
        else if( weight < 70){
            if(height < 165) return 3;
            else if(height < 175) return 1;
            else if(height >= 175) return 2;
        }
        else{
            if(height < 165) return 2;
            else if(height < 175) return 3;
            else if(height >= 175) return 1;
        }
    }
    else{         // 여자
        if( weight < 50 ){
            if(height < 165) return 1;
            else if(height < 175) return 2;
            else if(height >= 175) return 3;
        }
        else if( weight < 60){
            if(height < 165) return 3;
            else if(height < 175) return 1;
            else if(height >= 175) return 2;
        }
        else{
            if(height < 165) return 2;
            else if(height < 175) return 3;
            else if(height >= 175) return 1;
        }
    }
    return -1;
}

int main(){

    st std[10];
    int g1=0,g2=0,g3=0;
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++){

        scanf("%d %d %d",std[i].sex,std[i].weight,std[i].height);
        std[i].grade = checkGrade(std[i].sex,std[i].weight,std[i].height);

        if (std[i].grade == 1) g1++;
        else if (std[i].grade == 2) g2++;
        else if (std[i].grade == 3) g3++;
    }
    printf("%d %d %d",g1,g2,g3);
    return 0;
}

*//*


#include <stdio.h>
#include <string.h>
#pragma warning(disable:4996)
int main() {
    char str1[100], str2[100], str[10][100] = { '\0' };
    int i = 0, j = 0, k = 0, len = 0, cnt = 0, a = 0;

    gets(str1);
    while (str1[len]) {
        if (str1[len] == ' ') {
            cnt++;
            j = 0;
            len++;
            continue;
        }
        str[cnt][j] = str1[len];
        j++;
        len++;
    }//분리 완료
    for (i = 0; i <= cnt; i++) {
        puts(str[i]);
    }//출력

    printf("\n");
    cnt++;
    for (i = 0; i < cnt - 1; i++) {
        for (j = 0; j < cnt - (i+1); j++) {
            for (k = 0; k < len; k++) {
                if (strcmp(str[j],str[j+1]) > 0) {
                    strcpy(str2, str[j]);
                    strcpy(str[j], str[j + 1]);
                    strcpy(str[j + 1], str2);
                }
            }
            for (int q = 0; q <= cnt; q++)
                puts(str[q]);
            printf("\n////");
        }
    }


    return 0;
}*/
