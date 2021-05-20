import concurrent.futures
from multiprocessing import freeze_support
import math
import os

def is_prime(n):
    process_id = os.getpid()
    return process_id

def main(PRIMES):
    with concurrent.futures.ProcessPoolExecutor(max_workers=6) as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))
           

if __name__ == '__main__':
    freeze_support()
    main(PRIMES)
