#include<iostream>
using namespace std;

int fact(int n){
	int fact=1;
	for(int i=2;i<=n;i++){
		fact=fact*i;
	}
	return fact;
}
int main()
{
int n,r;
cin>>n>>r;
int ans=fact(n)/(fact(n-r)*fact(r));
cout<<ans<<endl;
}

