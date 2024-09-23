#include<iostream>
using namespace std;
int main(){
	int a=1,b=2;
	char op;
	cout<<"enter + or - operator";
	cin>>op;
	
	switch(op){
		case '+' : cout<<a+b;
		break;
		case '-': cout<<a-b;
		break;
		default : cout<<"i only know two operators";
		break;
	}

	return 0;
}
