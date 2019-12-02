#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include "malloc.h"

const int size=100; 	//size of array

int main()
{

float *p,*a;

p=(float*)malloc(size*sizeof(float));	//p is pointer to the block of memory allocated by malloc


for(int i=1;i<=size;++i)		//this loop store the values in the array whose pointer is p
{
	p[i-1]=i*i;
}

a=fun(p);			// 'fun' is the function which calculate mean and variance 

printf("mean=%0.2f\nvariance=%0.2f\n",*a,*(a+1));

free(p);
}
