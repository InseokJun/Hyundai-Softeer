# Attendance Tracking System ⏰

## Problem Overview ⌚

As an HR staff member, you want to track the attendance of each employee.

Since your company has implemented a flexible working hours system, the exact time when each employee arrives is not crucial.    
What matters is the total working time, which should not exceed the legal working hours and should meet the contracted time between the company and the employee.

The working hours for each employee are defined as the time between arrival and departure for a given day.      
Note that non-working hours, such as meal breaks, are not excluded from the total working hours.

Given the arrival and departure times for each day from Monday to Friday for an employee who has not taken any days off, write a program to calculate the total minutes worked over the 5 days.


## Constraints 🕰️

- All given numbers are integers.
- $1 \leq N \leq 100,000$
- $\sum^{N}_{i=1} A_i \leq 50000\$
- For all $i, j$ ($1 \leq i \leq N, 1 \leq j \leq A_i$), $1 \leq S_{i,j}, P_{i,j} \leq 10^9$
- $1 \leq M \leq 100,000$
- For all $k$ ($1 \leq k \leq M$), $1 \leq Q_k \leq 10^9$

## Input Format 🚜

1. First line: $N$ (total number of consumers)
2. Next $N$ lines: Consumer proposals
    - Format for each line $i$ ($1 \leq i \leq N$): $A_i S_{i,1} P_{i,1} \ldots S_{i,A_i} P_{i,A_i}$
3. Next line: $M$ (number of scenarios)
4. Last line: $M$ integers representing $Q_1, Q_2, \ldots, Q_M$ (separated by a single space)

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

