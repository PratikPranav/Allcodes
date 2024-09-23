#include<iostream>
using namespace std;
/* half inverted 12345  triangle
int main()
{
   int n;
   cin>>n;
   for(int i=1;i<=n;i++){
   	for(int j=1;j<=n+1-i;j++){
   		cout<<j<<" ";
	   }
	   cout<<endl;
   }

}
   //OR 
int main()
{
   int n;
   cin>>n;
   for(int i=n;i>=1;i--){
   	for(int j=1;j<=i;j++){
   		cout<<j<<" ";
	   }
	   cout<<endl;
   }

}*/
/*  half inverted triangle 1010101
int main(){
	int n;
	cin>>n;
	for(int i=1;i<=n;i++){
		for(int j=1;j<=i;j++){
			if((i+j)%2==0)
	           cout<<" 1 ";
	        else
	           cout<<" 0 ";
		}
		cout<<endl;
	}
}
*/
/*rhombus
int main()
{
	int n;
	cin>>n;
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n-i;j++){
			cout<<"  ";
		}
		for(int j=1;j<=n;j++){
			cout<<" * ";
		}
		cout<<endl;	
	}
}
*/
/*pyramid 1111 2222 3333
int main()
{
	int n;
	cin>>n;
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n-i;j++){
			cout<<" ";
		}
		for(int j=1;j<=i;j++){
			cout<<j<<" ";
		}
		cout<<endl;	
	}
}

*/
/*diamond pattern *
int main(){
	int n;
	cin>>n;
	//upper part
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n-i;j++)
		{
			cout<<"   ";
		}
		for(int j=1;j<=2*i-1;j++) //for printing odd nos of stars eg 1star, then 2star, 3,4...
		{
			cout<<" * ";
		}
		cout<<endl;
	}
	//lower part
		for(int i=n;i>=1;i--){  //reverse
		for(int j=1;j<=n-i;j++)
		{
			cout<<"   ";
		}
		for(int j=1;j<=2*i-1;j++) //for printing odd nos of stars eg 1star, then 2star, 3,4...
		{
			cout<<" * ";
		}
		cout<<endl;
	}
	
}
*///zig zag pattern
/*
int main()
{
	int n;
	cin>>n;    //stars are equal to n
	for(int i=1;i<=3;i++){  //3columns if fixed
		for(int j=1;j<=n;j++){     //column is till n
		if(((i+j)%4==0) || (i==2 && j%4==0))
		cout<<" * ";
		else
		cout<<"   ";
	}cout<<endl;
 }
} 
*/




