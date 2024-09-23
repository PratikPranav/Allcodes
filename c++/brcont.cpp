#include<iostream>
using namespace std;

int main()
{
	int pm=500;
	for(int i=1;i<30;i++){
		if(i%2==0){
				continue ;//skip to next iteration of the loop
		}
	if(pm==0){
		break;//terminate the loop
	}
		 cout<<"u can go";
		 pm=pm-500;
	}
	return 0;
}
