# Calculate Score Average 🎓

## Problem Overview 📊

The grades of N students are given in order of student ID.    
Write a program to calculate the average of the students' grades within the given range [A, B].

## Constraints 📈
- An integer $N where 1 ≤ N ≤ 10^6$
- An integer $K where 1 ≤ K ≤ 10^4$
- An integer $S_i where 1 ≤ S_i ≤ 100$
- Integers $A_i$ and $B_i$ where $1 ≤ A_i ≤ B_i ≤ N$

## Input Format 📉

The first line contains the number of students $N$ and the number of intervals $K$.
The second line provides the grades $S_i$ of each student for $i$ ranging from $1$ to $N$.
For each i + 2 ($1 ≤ i ≤ K$) line, the i-th interval $A_i$, $B_i$ is given.

## Output Format 📚

On the i-th line, output the average grade of the i-th interval (rounded to the third decimal place).  
If the difference is within 0.01, it will be considered as the correct answer.

## Example 📖

### Example Input 
```
5 3
10 50 20 70 100
1 3
3 4
1 5
```

### Example Output 
```
26.67
45.00
50.00
```


### Result Image

<img width="300" alt="스크린샷 2023-12-25 165353" src="https://github.com/InseokJun/Hyundai-Softeer/assets/153903563/509449fb-97ae-48c1-b2db-94184e947c7a">
<img width="300" alt="스크린샷 2023-12-25 165447" src="https://github.com/InseokJun/Hyundai-Softeer/assets/153903563/5d482084-2fbb-46da-a573-43f584c9dd1c">
<img width="300" alt="스크린샷 2023-12-25 165507" src="https://github.com/InseokJun/Hyundai-Softeer/assets/153903563/212673e5-c6dd-452a-bd56-c72e1294d2b9">



---
**Note**    
The provided statement suggests referring to the `Practice_Problem_Score_Average_Solution.txt` file for detailed explanations and descriptions of the implemented code.


