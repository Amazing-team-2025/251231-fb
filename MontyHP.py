'''
I could understand the explanation of the Monty Hall problem
but needed some more evidence

References:
  http://www.bbc.co.uk/dna/h2g2/A1054306
  http://en.wikipedia.org/wiki/Monty_Hall_problem especially:
  http://en.wikipedia.org/wiki/Monty_Hall_problem#Increasing_the_number_of_doors
'''
from random import randrange

doors, iterations = 3,100000  # could try 100,1000
