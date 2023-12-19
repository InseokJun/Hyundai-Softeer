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

## Output Format 🕘

The first line outputs the total working hours of the employee in minutes.


## Example ⏰🕰️⌚

### Example Input 1
```
10:00 19:00
09:00 15:00
10:00 11:00
11:00 22:00
09:00 15:00
```

### Example Output 1
```
1980
```

### Example Input 2
```
09:17 18:34
09:17 18:34
09:17 18:34
09:17 18:34
09:17 18:34
```

### Example Output 2
```
2785
```

### Example Input 3
```
09:17 19:24
10:11 18:45
09:34 18:27
10:47 15:33
08:47 18:32
```

### Example Output 3
```
2525
```

### Result 
<img width="300" alt="스크린샷 2023-12-20 011329" src="https://github.com/InseokJun/Hyundai-Softeer/assets/153903563/05b017cb-a750-4fdf-9ff1-1ae52a723ab2">
<img width="300" alt="스크린샷 2023-12-20 011357" src="https://github.com/InseokJun/Hyundai-Softeer/assets/153903563/cb0394aa-df4c-41b8-8626-827ffb49d90c">
<img width="300" alt="스크린샷 2023-12-20 011438" src="https://github.com/InseokJun/Hyundai-Softeer/assets/153903563/ce4659e6-72df-4a15-bfc4-06d53505ef29">
<img width="500" alt="스크린샷 2023-12-20 012510" src="https://github.com/InseokJun/Hyundai-Softeer/assets/153903563/5cba9c48-4ffe-46f8-a953-142aaa200280">
<img width="500" alt="스크린샷 2023-12-20 012541" src="https://github.com/InseokJun/Hyundai-Softeer/assets/153903563/b314cb0f-fc3b-4e7b-a160-d0795219fab9">

---
**Note**    
The provided statement suggests referring to the `Practice_Problem_Time_Solution.txt` file for detailed explanations and descriptions of the implemented code.
