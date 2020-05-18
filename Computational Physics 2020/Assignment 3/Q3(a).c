/*This code calculate the fourier transform and store the data in the filename "Q3.txt" 
this data is then plotted in python and compared with analytical fourier transform

To compile the code use: gcc Q3.c -lm -lgsl -lgslcblas*/

#include <stdio.h>
#include <math.h>
#include <gsl/gsl_errno.h>
#include <gsl/gsl_fft_complex.h>
#include<complex.h>

#define REAL(z,i) ((z)[2*(i)])
#define IMAG(z,i) ((z)[2*(i)+1])

int
main (void)
{
  int i;
  const int n = 256;
  double data[2*n];
  float x[n],dx,a=-100,b=100,L;
  L=b-a;
  dx=(b-a)/n;

  gsl_fft_complex_wavetable * wavetable;
  gsl_fft_complex_workspace * workspace;
	
  
  for (int i=0;i<n;++i)
	{
	x[i]=a+i*dx;
	//printf("x[%d]=%f\n",i,x[i]);
	}


  for (i = 0; i < n; i++)
    { if (x[i] == 0)
		{
      		REAL(data,i) = 1.0;
      		IMAG(data,i) = 0.0;
		}
	  else
		{
			REAL(data,i) = sin(x[i])/x[i];
      		IMAG(data,i) = 0.0;		
			
		}
    }

  /*
  for (i = 0; i < n; i++)
    {
      printf ("%f: %e %e\n", x[i], REAL(data,i),
                                IMAG(data,i));
    }
  printf ("\n");
	*/

  wavetable = gsl_fft_complex_wavetable_alloc (n);
  workspace = gsl_fft_complex_workspace_alloc (n);

  gsl_fft_complex_forward (data, 1, n,
                           wavetable, workspace);

  float freq[n];
  for (int i=0; i<n;++i)
	{
	  if (i < n/2)
		freq[i] = 2*M_PI*i/L;
	  else
		freq[i] = -2*M_PI*(n-i)/L;
	}

  char fname[50];
  sprintf(fname,"Q3.txt");
  FILE *fp=fopen(fname,"w");
  double complex factor;
  
  for(int i=0; i<n; ++i)
	{
	factor = dx*sqrt(1.0/(2*M_PI))*cexp(-I*freq[i]*a);
	//printf("%f\n",creal(factor));
	REAL(data,i)=REAL(data,i)*creal(factor) - IMAG(data,i)*cimag(factor);

	IMAG(data,i)=IMAG(data,i)*creal(factor) + REAL(data,i)*cimag(factor);
    fprintf(fp,"%f  %f \n",freq[i],REAL(data,i));
	//printf("%0.20f\t%0.20f\n",freq[i],REAL(data,i));
	}
 

   /*
  for (i = 0; i < n; i++)
    {
      printf ("%d: %e %e\n", i, REAL(data,i),
                                IMAG(data,i));
    }
  */

  gsl_fft_complex_wavetable_free (wavetable);
  gsl_fft_complex_workspace_free (workspace);
  return 0;
}
