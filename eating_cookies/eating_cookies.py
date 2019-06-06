#!/usr/bin/python

import sys

cache = {0: 1, 1: 1, 2: 2} # memoization

def eating_cookies(n, nothing=None):
  global cache

  # val is already calculated
  if n in cache:
    return cache[n]
  
  # calc value, cache it, return 
  cache[n] = eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)
  return cache[n]

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')