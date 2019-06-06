#!/usr/bin/python

import argparse

def find_max_profit(prices):
  """
  INPUT: a list of stock prices
  OUTPUT: the MAX profit that can be made from a single buy and single sell
  """

  # input coverage
  if len(prices) < 2:
    return "Must enter at least 2 prices"
  
  # Init vars
  buy =  1000000
  sell = 0
  buy_index = 0
  sell_index = 0
  max_profit = 0

  # iterate over prices
  for i in range(0, len(prices)):

    # find lowest price in list, note the index (can buy the last one either, bc then you coudn't sell!)
    if prices[i] < buy and i != len(prices) - 1:
      buy = prices[i]
      buy_index = i

    # find highest price in list after the buy list
    if prices[i] > sell and i > buy_index:
      sell = prices[i]
      sell_index = i
      
  max_profit = sell - buy

  return max_profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()
  print(args)
  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
