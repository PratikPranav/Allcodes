#include <iostream>
#include <string.h>
using namespace std;

typedef struct dfa
{
    int nos, nois, nofs;
    int final[10];
    int delta[10][10];
    int inpsmb[10];
}dfa;
int checksmb(char ch,dfa d){
    for(int i=0;i<d.nois;i++)
    {
        if(ch==d.inpsmb[i])
        return i;
    }
    return -1;
}
int checkfinalstate(int st,dfa d){
    for(int i=0;i<d.nofs;i++)
    {
        if(st==d.final[i])
        return 1;
    }
    return 0;
}
int main(){
    dfa d;
    cout<<"enter no of staes "; cin>>d.nos;
    cout<<"enter no of ip symbols "; cin>>d.nois;
    cout<<"enter no of final staes "; cin>>d.nofs;

    for(int i=0;i<d.nois;i++)
    {
         cout<<"ip smb"<<i; cin>>d.inpsmb[i];
    }
     for(int i=0;i<d.nofs;i++)
    {
         cout<<"final state"<<i; cin>>d.final[i];
    }
    cout<<"enter transitions:";
    for(int i=0;i<d.nos;i++)
    {
        for(int j=0; j<d.nois;j++)
        {
            cout<<"q"<<i<<"X"<<d.inpsmb[j];
            cin>>d.delta[i][j];
        }
    }
    for(int i=0;i<d.nois;i++)
    {
         cout<<d.inpsmb[i];
    }
    for(int i=0;i<d.nos;i++)
    {
        for(int j=0; j<d.nois;j++)
        {
            cout<<"q"<<i<<"X"<<d.inpsmb[i];
            cout<<d.delta[i][j];
        }
    }
    
}
do{
        char string[10];
        cout<<"enter a string";
        cin>>string;
        int statecount = 0;
        int flag=0;
        for(int i=0;i<strlen(string);i++)
        {
int sympos = checksmb(string[i],d);
if(sympos==-1){
    flag=0; break;
}
statecount = d.delta[statecount][sympos];
        }
if(flag==1 && checkfinalstate(statecount,d)==1)
{
    cout<<"string accepted";
}
else cout<<"not";

        
    }while(1);
    return 0;
}
     
