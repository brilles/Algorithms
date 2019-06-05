#!/usr/bin/python

import argparse

def find_max_profit(prices):

  """
    INPUT: a list of stock prices
    OUTPUT: the maximum profit that can be made from a single buy and sell
  """

  # invalid input coverage
  if len(prices) < 2:
    return "You must enter at least 2 prices"
  # input is valid
  else: 
    # init varst
    profit = None
    smallest = prices[0]
    smallestIndex = 0
    largestIndex = 0
    largest = 0

    for i in range(0, len(prices) - 1):
      if prices[i] < smallest:
        smallest = prices[i]
        smallestIndex = i
    for i in range(smallestIndex, len(prices) - 1):
      if prices[i] > largest:
        largest = prices[i]
        largestIndex = i

    # calculate diff
    print("LARGEST", largestIndex, largest, prices)
    print("SMALLEST", smallestIndex, smallest, prices)
    
    profit = largest - smallest
    if smallestIndex > largestIndex:
      return profit * -1
    return profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()
  print(args)
  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

# print(find_max_profit([1050, 270, 1540, 3800, 2])) #should return 3530