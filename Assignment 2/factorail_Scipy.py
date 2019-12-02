import timeit

from scipy.special import factorial

num = int(input("Enter a number whose factorail you want to find out\n: ")) 

start = timeit.default_timer()
print("Factorial of",num,"is",factorial(num))
stop = timeit.default_timer()
print('Time taken in second :', stop - start)  





