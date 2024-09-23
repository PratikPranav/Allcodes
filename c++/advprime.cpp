#include<iostream>
using namespace std;
#include<cmath>

/*normal prime
int main()
{
int n;
cin>>n;
bool flag=0;    //to know that is we going out of loop by finishing the loop or by break
for(int i=2;i<=n;i++){
	if(n%i==0)   cout<<"non prime" ;  //because more than 2 factor ,eg 1,2,itself
    flag=1;   break;
}
if(flag==0)   //flag =0 that means we have fully finished the loop and then came out
	cout<<"prime"<<endl;

}
*/
/*advance (less time complexity) (sqrt) prime
int main()
{
int n;
cin>>n;
bool flag=0;    //to know that is we going out of loop by finishing the loop or by break
for(int i=2;i<sqrt(n);i++){
	if(n%i==0)   cout<<"non prime" ;  //because more than 2 factor ,eg 1,2,itself
    flag=1;   break;
}
if(flag==0)   //flag =0 that means we have fully finished the loop and then came out
	cout<<"prime"<<endl;

}
*/
