'''
We already have a fucntion to find factorial defined in c 'factorial_fuction.c', we would use this function in python.
1st create a 'testlib.so' file by typing "gcc -shared -o testlib.so -fPIC factorial_fuction.c" on the terminal.


'''
import ctypes
import timeit

num = int(input("Enter the number of which you want to find out factorial: "))
so_file = "/home/ankit/Desktop/Assignment2_Numerical_technique/testlib.so" #this is the path of testlib.so file you genrated
f = ctypes.CDLL(so_file)

start = timeit.default_timer()
factorial = f.factorial(num)
stop = timeit.default_timer()

print("Factrial of",num,"is",factorial)

print("total time taken =",stop-start,"sec")
