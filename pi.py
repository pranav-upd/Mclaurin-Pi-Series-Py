import math

itr = int(input("Enter the number of iterations you want to run the program:"))
pi_val, x, y, z =  0, 0, 0, 0


def doublefact(z):
    return math.prod(range(z, 0, -2))
    


for x in range(itr):
    dfact_val = doublefact(2*x)
    double_fact_val = doublefact(2*x - 1)
    pi_val += 6*((double_fact_val*(10**itr))//((2**(2*x+1))*(dfact_val*(2*x+1))))

with open("pi.txt", "w") as pi_file:
    pi_file.write(str(pi_val)[:(len(str(pi_val))//2)])
