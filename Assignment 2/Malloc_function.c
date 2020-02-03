#include <stdio.h>
#include "malloc.h"
#include<math.h>


float * fun(float *p)			
{	float size=100;
	static float out[2], mean=0.0,variance=0.0;		//out[2] is the local array so its adress can't be passed to the main, for this reason we choose static but you can also define array with malloc that would also work
	for(int i=0;i<size;++i)
	{
		mean+=p[i];
	}
	mean=mean/size;
	for(int i=0;i<size;++i)
	{
		variance+=pow((p[i]-mean),2);
	}
	variance=variance/size;
	out[0]=mean;
	out[1]=variance;
	
	return out;
}

