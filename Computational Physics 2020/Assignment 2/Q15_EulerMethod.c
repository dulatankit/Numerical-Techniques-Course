#include<stdio.h>
#include<math.h>
int main()
{
int N=10,i;
float a=0,b=2,h,w,y[N+1],t,x[N+1],z,M;

h=(b-a)/N;
t=a;
w=y[0]=0.5;
float f(float t, float w)
	{
		return 	(w-t*t+1);
	}

for(i=1;i<=N;++i)
{
	w=w+h*f(t,w);
	y[i]=w;
	t=a+i*h;
	//z=pow(t+1,2)-0.5*exp(t);
	//printf("y=%f\tt=%f\n",w,t);
	//printf("value=%f\tt=%f\n",z,t);
	
}
printf("time (t)\tEuler Solution\tActual Error\tError Bound\n\n");
for(int j=1; j<=N;++j)
{
	t=a+j*h;
	z=pow(t+1,2)-0.5*exp(t);
	M=0.1*(0.5*exp(2)-2)*(exp(t)-1);	
	printf("%f\t%f\t%f\t%f\n",t,y[j],fabs(y[j]-z),M);
}
}

