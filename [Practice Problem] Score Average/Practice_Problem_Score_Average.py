"""
Question - Calculate Score Average
"""

student_num, avg_section = map(int, input().split())             # Receive input data according to the input format

score = list(map(int, input().split()))                          # Receive input data according to the input format


for _ in range(avg_section):                                     # Repeat as many times as there are number of sections
  
  section_start, section_end = map(int, input().split())         # Receive input data according to the input format

  print(round(sum(score[(section_start - 1):section_end]) / (section_end - section_start + 1), 2))    # Calculate Score Average and Round Result