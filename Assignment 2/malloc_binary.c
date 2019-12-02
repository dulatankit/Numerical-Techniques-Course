/*This code define an array with Malloc and assign the array with loops and the uses a function to generate an array whose elements are 'mean' and 'variance'.This output is printed on the 'terminal' as well store in a binary file whose path and filename must be fed by user(e.g. /home/ankit/Desktop/Malloc.txt) and then we also print the data stored in this file on the terminal.
*/

#include<stdio.h>
#include<stdlib.h>
#include<math.h>

const int size=100; 	//size of array

float *fun(float *arr);   //fuction prototype-it returns pointer to an array and argument is also pointer to an array

int main()
{

float *p,*a;
FILE *fp;

p=(float*)malloc(size*sizeof(float));	//p is pointer to the block of memory allocated by malloc


for(int i=1;i<=size;++i)		//this loop store the values in the array whose pointer is p
{
	p[i-1]=i*i;
}

a=fun(p);			// 'fun' is the function which calculate mean and variance 

char path[100],data[50];

printf("enter the path where you want to create the file + filename.bin(extension should be bin)\n");
scanf("%s",path);
fp=fopen(path,"wb");
fprintf(fp,"mean=%f\nvariance=%f\n",*a,*(a+1));
fclose(fp);

fp=fopen(path,"rb");
printf("data inside binary file is\n");
while(fscanf(fp,"%s",data)!=EOF) 
{
	printf("%s\n",data);
}

printf("I checked the size of both files by typing 'du -a -h filename', it showed that both file are of same size 4k. but i checked with fuction 'ftell' it showed that binary file is small, so for large amount of data , binary file would be good\n");
free(p);
}

float * fun(float *p)			
{
	static float out[2], mean=0.0,variance=0.0;		//out[2] is the local array to store mean and variance
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




