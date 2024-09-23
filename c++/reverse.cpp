#include<iostream>
using namespace std;

int main()
{
  int n;
  cin>>n;
  
  int rev=0;
  while(n>0){
  	int lastdigit=n%10;  //lastdigit==remainder of the number
  	rev = rev*10 + lastdigit;  //eg. 4*10 =40+3(lastdigit)=43. and so on 4321.
  	n=n/10;    //to get remaining no. after removing last digit. eg 1234 then 123 then 12 ...
  }
  cout<<rev<<endl;

}

