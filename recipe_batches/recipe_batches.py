#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  max_produce_max = 100000
  for key, value in recipe.items():
    try:
      val = ingredients[key]
      max_produce = val//value
      if max_produce < max_produce_max:
        max_produce_max = max_produce
    except: 
      return 0
  return max_produce_max

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))