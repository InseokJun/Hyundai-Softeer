"""
Question - Compare Driven Distance 
"""

"""Answer 1"""
distance_list = list(map(int, input().split()))         # Receive input data according to the input format

if distance_list[0] < distance_list[1]:                 # Compare B Longer than A
  print("B")

elif distance_list[1] < distance_list[0]:               # Compare A longer than B
  print("A")

else:                                                   # Equal A and B
  print("same")
  
"""Answer 2"""
a, b = map(int, input().split())                        # Receive input data according to the input format

if b < a:                                               # Compare A longer than B
  print("A")

elif a < b:                                             # Compare B Longer than A
  print("B")    

else:                                                   # Equal A and B
  print("same")