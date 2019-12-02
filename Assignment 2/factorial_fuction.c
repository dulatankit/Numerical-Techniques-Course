#include<stdio.h>
// function which find the factorial of a number with recurssion
int facto(int a) 		
{long int y;
 if(a==0)
  y=1;
else 
y=a*facto(a-1);
return(y);
}

