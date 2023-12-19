"""
Question - Find the working hours in minutes from Monday to Friday
"""

# Declare Variable 
work_day = 5                                                            # Number of days worked in a week
total_work_min = 0                                                      # Minutes per week worked

# Solve the Question
for _ in range(work_day):                                               # Repeat as many days as the input format
    
    temp = list(map(int, input().replace(":", " ").split(" ")))         # Manipulate input data considering the input format
    
    total_work_min += (temp[2] * 60+temp[3]) - (temp[0] * 60+temp[1])   # Calculate total work time
    
# print output
print(total_work_min)
    