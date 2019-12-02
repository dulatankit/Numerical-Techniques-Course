#include<stdio.h>
#include<float.h>
#include<math.h>
int main()
{
printf("epsilon for C float is :%e\n",FLT_EPSILON);

float y= 3.1415926535,x=2.0,RE1,RE2;

RE1=(fabs(y-3.1415926535))/3.1415926535;		// where pi is used upto 10 decimal places
RE2=(fabs(x-2.0))/2.0;

printf("Relative error in storing Pi is %.3e  \n",RE1);
printf("Relative error in storing 2.0 is %.3e  \n",RE2);

printf("pi is not a machine number for float data type but 2.0 is a machine number\n");

}


