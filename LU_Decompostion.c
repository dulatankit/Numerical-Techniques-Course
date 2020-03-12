#include<stdio.h>
#include<gsl/gsl_matrix.h>
#include<gsl/gsl_permutation.h>
#include<gsl/gsl_linalg.h>

int main()
{
const int m=3,n=3;

gsl_matrix *A=gsl_matrix_alloc(m,n);
double a[]={1,0.67,0.33,0.45,1,0.55,0.67,0.33,1};
//gsl_matrix *U=gsl_matrix_alloc(3,3);
//gsl_matrix *L=gsl_matrix_alloc(3,3);
float L[m][m],U[m][m];
printf("Input matrix is A\n");
for(int i=0; i<m;++i){
	for (int j=0;j<n;++j)
		{
			gsl_matrix_set(A,i,j,a[3*i+j]);
			printf("%g\t",gsl_matrix_get(A,i,j));
		}
	printf("\n");}
gsl_permutation * p=gsl_permutation_alloc(m);
int s;
gsl_linalg_LU_decomp(A,p,&s);


printf("Matrix U is:\n");
for(int i=0; i<m;++i){
	for (int j=0;j<n;++j)
		{
			if(j>=i){			
			printf("%g\t",gsl_matrix_get(A,i,j));
			//gsl_matrix_set(U,i,j,gsl_matrix_get(A, i, j));
			U[i][j]=gsl_matrix_get(A,i,j);}
			else{
			printf("0\t");//gsl_matrix_set(U,i,j,0);
			U[i][j]=0;}
		}
	printf("\n");}

printf("Matrix L is:\n");
for(int i=0; i<m;++i){
	for (int j=0;j<n;++j)
		{
			if (j<i){
			printf("%g\t",gsl_matrix_get(A,i,j));
			//gsl_matrix_set(L,i,j,gsl_matrix_get(A, i, j));
			L[i][j]=gsl_matrix_get(A,i,j);}
			else if (j==i){ printf("1\t"); //gsl_matrix_set(L,i,j,1);
					L[i][j]=1;}
			else {printf("0\t"); //gsl_matrix_set(L,i,j,0);
				L[i][j]=0;}
		}
	printf("\n");}

printf("Product of LU is:\n");
float x;
for (int i=0;i <3;++i){
	for (int j=0;j<3;++j){
		x=0;
		for (int k=0; k<3;++k){
			//x+=gsl_matrix_get(L,i,k)*gsl_matrix_get(U,k,j);
			x+=L[i][k]*U[k][j];}
		printf("%f\t",x);}
	printf("\n");}	




}
