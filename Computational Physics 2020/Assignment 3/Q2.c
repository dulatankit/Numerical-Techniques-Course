#include<stdio.h>
#include<math.h>
#include<fftw3.h>
#include<complex.h>


//void f(float x[], int N, float out[N][2]); 


int main()
{
int N=256;
float x[N],dx,a=-100,b=100,L;
L=b-a;
dx=(b-a)/N;

fftw_complex *in, *out;
fftw_plan p;


in = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);
out = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);
p = fftw_plan_dft_1d(N, in, out, FFTW_FORWARD, FFTW_ESTIMATE);


for (int i=0;i<N;++i)
{
	x[i]=a+i*dx;
	//printf("x[%d]=%f\n",i,x[i]);
}

for(int i=0;i<N;++i)
{
			if (x[i] == 0)
				{in[i][0]=1;
				in[i][1]=0;}
			else 
				{in[i][0] = sin(x[i])/x[i];
				in[i][1] = 0;}
}

/*
for(int i=0; i<N;++i)
{
printf("%0.20f\t%0.20f\n",x[i],in[i][0]);
}
*/

fftw_execute(p);

float freq[N];
for (int i=0; i<N;++i)
{
	if (i < N/2)
		freq[i] = 2*M_PI*i/L;
	else
		freq[i] = -2*M_PI*(N-i)/L;
}

double complex factor;
printf("frequency\t\tintensity\n");
for(int i=0; i<N; ++i)
{
	factor = dx*sqrt(1.0/(2*M_PI))*cexp(-I*freq[i]*a);
	//printf("%f\n",creal(factor));
	out[i][0]=out[i][0]*creal(factor) - out[i][1]*cimag(factor);

	out[i][1]=out[i][1]*creal(factor) + out[i][0]*cimag(factor);
	printf("%0.20f\t%0.20f\n",freq[i],out[i][0]);
}
fftw_destroy_plan(p);
fftw_free(in); fftw_free(out);
}

