#include<iostream>
#include<cmath>
using namespace std;

bool isPrime(int num){
	for(int i=2;i<=sqrt(num);i++){
		if(num%i==0)   //non prime
		return false;
	}
	return true;    // code fully completed and its thus a prime no.
}
int main()
{
  int a,b;
  cin>>a>>b;
  for(int i=a;i<=b;i++){
  if(isPrime(i))
  cout<<i<<endl;
  }
  return 0;

}

