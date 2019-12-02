#include<stdio.h>
#include<time.h>

int facto (int a);

int facto(int a) 		// function which find the factorial of a number with recurssion
{long int y;
 if(a==0)
  y=1;
else 
y=a*facto(a-1);
return(y);
}


int main()
{
	int n;
	long int y;
	double t;
	time_t start,end;
    printf("enter the no whose factorial you want to find out:\n");
    scanf("%d",&n);
	start=clock();
	for(int i=0; i<50; ++i)
	{
    	y=facto(n);
	}
	end=clock();
	t=(double)(end-start)/((CLOCKS_PER_SEC)*50);
    printf("value of %d!=%ld\n",n,y);
	printf("time taken to calculate the factorial = %e sec\n",t);
}

