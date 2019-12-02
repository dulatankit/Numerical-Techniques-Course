#include<stdio.h>
#include<limits.h>	//in this headerfile limit fuction of integer numbers are defined
#include<float.h>  //in this headerfile limit function of floating numbers are defined
int main()
{
printf("size of 'char' : %ld byte\nsize of 'int' : %ld byte\nsize of 'long int' : %ld byte\nsize of 'float' : %ld byte\nsize of 'double' : %ld byte\n",sizeof(char),sizeof(int),sizeof(long int),sizeof(float),sizeof(double ));

printf("minimum no. on 'char' = %d\n", CHAR_MIN);
printf("maximum no. on 'char' = %d\n", CHAR_MAX);

printf("minimum no. on 'int' = %+d\n", INT_MIN);
printf("maximum no. on 'int'= %+d\n", INT_MAX);

printf("minimum no. on 'long int'= %+ld\n", LONG_MIN);
printf("maximum no. on 'long int'= %+ld\n", LONG_MAX);

printf("minimum no. on 'float'= %e\n", FLT_MIN);
printf("maximum no. on 'float'= %e\n", FLT_MAX);

printf("minimum no. on 'double' = %e\n", DBL_MIN);
printf("maximum no. on 'double' = %e\n", DBL_MAX);

}
