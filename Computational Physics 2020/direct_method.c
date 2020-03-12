// this code finds the LU decompostion of a given matrix and for checkig purpose 
// it reconstruct the original matrix

#include<stdio.h>
#include<gsl/gsl_matrix.h>
#include<gsl/gsl_permutation.h>
#include<gsl/gsl_linalg.h>
int main()
{
	const int n=3;
	int i,j;
	double a[9]={1.,0.67,0.33,0.45,1.,0.55,0.67,0.33,1.};
	gsl_matrix *A=gsl_matrix_alloc(3,3);
	for (i=0;i<3;i++)
		for (j=0;j<3;j++)
			gsl_matrix_set(A,i,j,a[3*i+j]);
	printf("Given Matrix:\n");
	for (i = 0; i < 3; i++) 
    		for (j = 0; j < 3; j++)
      		printf ("A(%d,%d) = %g\n", i, j,gsl_matrix_get(A,i,j));	
      gsl_permutation * p = gsl_permutation_alloc (3);
      int s;
      gsl_linalg_LU_decomp (A, p, &s);
      gsl_matrix *U=gsl_matrix_alloc(3,3);
      gsl_matrix *L=gsl_matrix_alloc(3,3);
      for (i=0;i<3;i++)
		for (j=0;j<3;j++)
			if(j>=i)
				gsl_matrix_set(U,i,j,gsl_matrix_get (A, i, j));
			else
				gsl_matrix_set(U,i,j,0.);
	printf("Upper traingular Matrix [U] of LU decomposition:\n");
	for (i = 0; i < 3; i++) 
    		for (j = 0; j < 3; j++)
      		printf ("U(%d,%d) = %lf\n", i, j,gsl_matrix_get (U, i, j));
      for (i=0;i<3;i++)
		for (j=0;j<3;j++)
			if(j<i)
				gsl_matrix_set(L,i,j,gsl_matrix_get (A, i, j));
			else if(j==i)
				gsl_matrix_set(L,i,j,1.);
			else
				gsl_matrix_set(L,i,j,0.);
     printf("Lower traingular Matrix [L] of LU decomposition:\n");
	for (i = 0; i < 3; i++) 
    		for (j = 0; j < 3; j++)
      		printf ("L(%d,%d) = %lf\n", i, j,gsl_matrix_get (L, i, j));
      double A_prime[3][3];
      for (i=0;i<3;i++)
      {
      	for (j=0;j<3;j++)
      	{
      		A_prime[i][j]=0.;
      		for (int k=0;k<3;k++)
      		{
      			A_prime[i][j]+=gsl_matrix_get(L,i,k)*gsl_matrix_get(U,k,j);
      		}
      	}
      }
      printf("A_prime [LU] Matrix:\n");
      for (i = 0; i < 3; i++) 
    		for (j = 0; j < 3; j++)
      		printf ("A_prime(%d,%d) = %lf\n", i, j,A_prime[i][j]);
}
