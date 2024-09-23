// #include <stdio.h>
// int main(){
//     int n,temp,rev=0;
//     printf("enter the no");
//     scanf("%d",&n);
//     temp = n;
//     while(temp!=0){
//         int rem=temp%10;
//          rev=rev*10+rem;
//         temp=temp/10;
//     }
//     if(rev==n)
//     printf("palindrome");
//     else
//     printf("not palindrome");
// }


#include<stdio.h>
int checkPalindrome(int number)
{
int temp=number,rev=0;
while (number!=0){
    int rem=number%10;
    rev=rev*10+rem;
    number=number/10;
      }
      if(rev==temp) return 0;
      else
      return 1;

}

int main()
{
  int number;

  printf("Enter the number: ");
  scanf("%d", &number);

  if(checkPalindrome(number) == 0)
  printf("%d is a palindrome number.\n",number);
  else
  printf("%d is not a palindrome number.\n",number);

  return 0;
}