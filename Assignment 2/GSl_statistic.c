/*This code uses GSL library function to calculate the mean and variance. To execute the code type 'gcc -Wall GSl_statistic.c -lm -lgsl -lgslcblas -o test' on the termimal it would create a objective file 'test', to execute this file type './test'. now you would got your result

*/
#include<stdio.h>
#include<stdlib.h>
#include <gsl/gsl_statistics.h>
int main()
{
	double *p;
	double mean,variance;
	p=(float*)malloc(100*sizeof(float));
	for(int i=1;i<=100;++i)
	{
		p[i-1]=i*i;
	}
	mean     = gsl_stats_mean(p, 1, 100);
    variance = gsl_stats_variance(p, 1, 100);
	printf ("The sample mean is %g\n", mean);
    printf ("The estimated variance is %g\n", variance);
	printf("Mean obtained from this method is same as we obtained earlier but the variance is different\n");

}
