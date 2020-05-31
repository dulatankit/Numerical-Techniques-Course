#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include <time.h> 

int main() 
{ 
    int  n = 10000,i; 
    float x[n],y[n],b=0.0;
    FILE *out_file = fopen("Q4.txt","w");
    //srand(time(0));
    for (i=0;i<n;i++)  //this loop genrate random numbers as well find maximum
    {
    	x[i]=rand();     
    	if (x[i]>b)
    	{
    		b=x[i];
		}
		
   	}
  
    //printf("%f\n",b);
    for (i=0;i<n;i++)    // this loop genrate random number for required distribution function 2exp(-2x)
    {
    	x[i]=x[i]/b;
    	y[i]=-0.5*log(1-x[i]);   //Transormation equation
    	fprintf(out_file,"%f\n",y[i]);
    	//printf("%f\n",y[i]);
	}
	
	
    return 0; 
} 
