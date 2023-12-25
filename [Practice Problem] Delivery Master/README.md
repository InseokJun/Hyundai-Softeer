# Delivery Master 🚚

## Problem Overview 🚐

Gwangwoo, who needed pocket money for a summer vacation, applied for a part-time job loading and unloading H-delivery packages.   
Gwangwoo, who usually doesn't exercise and lacks physical strength, wanted to minimize the weight he had to carry by manipulating the order of the rails where the packages are coming down.

There are N rails, and each rail is designated for a specific weight, denoted as Ni. (No rails with the same weight are given.)    
Once the order of the rails is determined, you have to load the packages onto the delivery basket in rail order until the weight of the basket exceeds the weight limit (M).     
If you can carry as much weight as possible without exceeding the weight limit, it is considered as one job done. (Note that you cannot skip the rail order, and packages must be loaded in sequence.)

Help Gwangwoo by creating a program that allows him to do the job K times with the minimum weight.

## Constraints 🚒
- $3 \leq N \leq 10$
- $max(N_i) < M ≤ 50$
- $1 ≤ K ≤ 50$
- $1 ≤ N_i ≤ 50$

## Input Format 🚜

The first line contains the number of rails N, the weight limit of the delivery basket M, and the number of work executions K. The next line contains the dedicated weights of $N_i$ packages for each rail. (There are no cases where the weight of the delivery basket is smaller than that of the packages.)

## Output Format 🚛

The output should print the minimum total weight of packages that Gwangwoo needs to carry for the given number of work executions.


## Example 🚚📦

### Example Input 1
```
5 20 4
5 8 10 19 7
```

### Example Output 1
```
54
```

### Example Input 2
```
9 25 50
1 21 2 22 3 23 4 24 10
```

### Example Output 2
```
772
```

### Result Image

---
**Note**    
The provided statement suggests referring to the `Practice_Problem_Delivery_Master_Solution.txt` file for detailed explanations and descriptions of the implemented code.

