import random

# main routines goes here

tokens = ["unicorn", "horse", "zebra", "donkey"]

# testing loop too generate 20 tokens
for item in range (0,20):
    chosen = random .choice (tokens)
    print(chosen, end='\t')
