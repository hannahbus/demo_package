import concurrent.futures
from multiprocessing import freeze_support
from numpy.linalg import inv
import math
import os
import numpy as np

def is_prime(n):
    process_id = os.getpid()
    return process_id

def main(PRIMES, workers):
    with concurrent.futures.ProcessPoolExecutor(max_workers= workers) as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))
               
def alternative(dim): 
    m = np.random.rand(dim, dim)
    m2 = m@m 
    m = inv(m)
    return True

def main_2(dim, workers): 
    with concurrent.futures.ProcessPoolExecutor(max_workers= workers) as executor:
           for number, prime in zip(dim, executor.map(alternative, dim)):
            print((number, prime))
            

if __name__ == '__main__':
    freeze_support()
    main_2(dim, workers)
