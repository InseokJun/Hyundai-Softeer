"""
Question - Calculate A + B
"""

case_num = int(input())                     # Receive the number of Case.

for i in range(case_num):                   # Repeat as many cases there are cases
    
  a, b = map(int, input().split())          # Receive Cases
  
  print(f"Case #{i+1}: {a + b}")            # Print Output 