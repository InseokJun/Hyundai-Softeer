# Attendance Tracking System ⏰

## Problem Overview ⌚

As an HR staff member, you want to track the attendance of each employee.

Since your company has implemented a flexible working hours system, the exact time when each employee arrives is not crucial.    
What matters is the total working time, which should not exceed the legal working hours and should meet the contracted time between the company and the employee.

The working hours for each employee are defined as the time between arrival and departure for a given day.      
Note that non-working hours, such as meal breaks, are not excluded from the total working hours.

Given the arrival and departure times for each day from Monday to Friday for an employee who has not taken any days off, write a program to calculate the total minutes worked over the 5 days.


## Constraints 🕰️

- Employees did not work overnight. In other words, the arrival and departure times occurred after 00:00 and before 24:00.

- The arrival and departure times are given in the format HH:MM.
- HH is one of 00, 01, 02, .., 22, 23.
- MM is one of 00, 01, 02, .., 58, 59.
- Employees worked for at least 1 minute every day.

## Input Format 🕐

1. The first line provides the arrival and departure times on Monday, separated by a single space.
2. The second line provides the arrival and departure times on Tuesday, separated by a single space.
3. The third line provides the arrival and departure times on Wednesday, separated by a single space.
4. The fourth line provides the arrival and departure times on Thursday, separated by a single space.
5. The fifth line provides the arrival and departure times on Friday, separated by a single space.

## Output Format 🚛

$M$ integers separated by a single space.

- If it's possible to achieve $Q_k$ won or more in revenue, output the minimum truck size.
- If it's not possible, output -1.


## Example 🚚🚛🚜🚒🚐

### Example Input 1
```
4                        # Number of Consumer
1 1 1                    # Number of Proposal  Size of Car  Spending Money
1 2 2
1 3 3
1 4 4
10
1 2 3 4 5 6 7 8 9 10
```

### Example Output 1
```
1 2 2 3 3 3 4 4 4 4
```

### Example Input 2
```
5
2 10 17 5 19
2 8 7 10 21
3 3 3 9 13 11 14
3 5 3 1 2 9 15
1 9 11
11
21 31 35 54 79 80 100 3 5 7 9
```

### Example Output 2
```
5 8 9 9 10 11 -1 3 3 5 5
```

---
**Note**    
The provided statement suggests referring to the `Annual_Employee_Competition_Final_21_Truck_Solution.txt` file for detailed explanations and descriptions of the implemented code.

