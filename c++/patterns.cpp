#include<iostream>
using namespace std;

//rectangle
/*
int main()
{
   int r,c;
   cin>>r>>c;
   for(int i=1;i<=r;i++){
   	for(int j=1;j<=c;j++){
   	cout<<" * ";
       }
       cout<<endl;
   }

}*/
/*hollow rect
int main()
{
   int r,c;
   cin>>r>>c;

   
   for(int i=1;i<=r;i++){
   	for(int j=1;j<=c;j++){
   		if(i==1 || i==r)
   	cout<<" * ";
   	else 
   	if(j==1 || j==c)
   	cout<<" * ";
   	else
   	cout<<"   ";
       }
cout<<endl;
   }

}
*/
/*invert half pyramid
int main(){
	int n;
	cin>>n;
	
	for(int i=n;i>=1;i--){
		for(int j=1;j<=i;j++){
			cout<<" * ";
		}
		cout<<endl;
	}
	
}
*/
/*half pyramid after 180 degree rotation 
//fist space and then * 
int main()
{
   int n;                                              //eg   n=3
   cin>>n;                                               //   _ _ *
   for(int i=1;i<=n;i++){                               //    _ * *
   	for(int j=1;j<=n;j++){                             //     * * *
   		if(j<=n-i)   //n-row put spaces
   	cout<<"   ";
   	else
   	cout<<" * ";
       }
       cout<<endl;
   }
}
*/
/*half pyramid with no = row no
int main()
{
   int n;                                              
   cin>>n;                                             
   for(int i=1;i<=n;i++){                              
   	for(int j=1;j<=i;j++){                             
   		cout<<i<<" ";
       }
       cout<<endl;
   }
}*/
int main()
{
	int n,count=1;
	cin>>n;
	for(int i=1;i<=n;i++)
	{
		for(int j=1;j<=i;j++){
			cout<<count<<" ";
			count++;
		}
	}cout<<endl;
}
