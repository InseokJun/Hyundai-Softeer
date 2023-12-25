"""
Qeustion - Calculate Minimum Box Weight
"""

import sys                                                      # To declare an arbitrary large value, import sys module
from itertools import permutations                              # To calculate Permutation, import permutation function

rail_num, basket_weight, work_num = map(int, input().split())   # Receive input data according to the input format

rail_weight_list = list(map(int, input().split()))              # Receive input data according to the input format

min_total_weight = sys.maxsize                                  # Initialization arbitrary large value

for rail in permutations(rail_weight_list, rail_num):           # Iterate the loop as many times as the number of permutations

  rail_idx = 0                                                  # Declare Variable that access rail list and Initialization
  work_count = 0                                                # Declare Variable that count work time and Initialization
  total_weight = 0                                              # Declare Variable that calculate total weight and Initialization
  basket_now_weight = 0                                         # Declare Variable that calculate now basket weight and Initialization

  rail = list(rail)                                             # One of the Permutation Cases change type to list
  
  while work_count != work_num:                                 # The loop continues until the specified number of iterations is reached
      
    if basket_now_weight + rail[rail_idx] <= basket_weight:     # Current basket combined with the next box, is lighter than the basket weight limit
      basket_now_weight += rail[rail_idx]                       # Accumulate the weight of the next box
      rail.append(rail[rail_idx])                               # Place the box that was just used back on the rail
      rail_idx += 1                                             # Go to Next Rail
      
    else:                                                       # Current basket weight is heavier than basket weight limit
      total_weight += basket_now_weight                         # Accumulate the current basket weight to the final total weight
      basket_now_weight = 0                                     # Initialization the basket now weight 
      work_count += 1                                           # Increase work count 

  min_total_weight = min(total_weight, min_total_weight)        # Compare what is the minimum weight 

# Print Output
print(min_total_weight)                                         