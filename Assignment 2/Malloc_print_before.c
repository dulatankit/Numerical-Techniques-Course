#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include "malloc.h"

const int size=100; 	//size of array

int main()
{
int k;
printf("For defining array,enter 1 to use malloc and 2 to use calloc\n");
scanf("%d",&k);
if(k==1)
{

float *p;

p=(float*)malloc(size*sizeof(float));
printf("array values with malloc before assigning to array\n");
for(int i=1;i<=size;++i)		
{
	printf("%0.2f\n",p[i-1]);
	p[i-1]=i*i;
}
}

else if(k==2)
{
float *p;
p=(float*)calloc(size,sizeof(float));
printf("array values with calloc before assigning to array\n");
for(int i=1;i<=size;++i)		
{
	printf("%0.2f\n",p[i-1]);
	p[i-1]=i*i;
}
}

printf("In both cases either we use Calloc or Malloc to assign an array the values of uninitialized array are zeroes");
}
