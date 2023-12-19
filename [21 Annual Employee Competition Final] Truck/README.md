# Truck Size Decision for Maximum Revenue 🚚

## Problem Overview 🚐

As a truck designer at Hyundai Motor Group, your task is to determine the size of a new truck. You conducted a survey of $N$ consumers, each providing multiple purchase proposals based on the truck's size.

Each consumer $i$ ($1 \leq i \leq N$) submitted $A_i$ proposals. Proposal $j$ ($1 \leq j \leq A_i$) from consumer $i$ states, "I am willing to purchase a truck at a price of $P_{i,j}$ won if the size is greater than or equal to $S_{i,j}$."

However, producing a customized truck for each consumer incurs significant facility costs. Therefore, you need to decide on a single truck size that satisfies various consumer proposals.

Since consumers won't purchase more than two trucks, you will either accept one proposal from each consumer or reject all proposals. The chosen truck size should maximize the total revenue.

To explore revenue scenarios, you plan to consider $M$ scenarios. For each scenario $k$ ($1 \leq k \leq M$), you need to find the minimum truck size to achieve a total revenue of at least $Q_k$ won.

## Constraints 🚒

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

### Result Image
<img width="500" alt="스크린샷 2023-12-19 232017" src="https://github.com/InseokJun/Hyundai-Softeer/assets/153903563/174f0ba3-0dde-4f45-a53e-c5f023d4bc13"> <img width="500" alt="스크린샷 2023-12-19 232029" src="https://github.com/InseokJun/Hyundai-Softeer/assets/153903563/e7f2620e-aceb-4ac0-88cd-331c665d6672">
<img width="500" alt="스크린샷 2023-12-19 232114" src="https://github.com/InseokJun/Hyundai-Softeer/assets/153903563/b8787a8a-4daf-4248-b25b-0c242549b9f3"><img width="500" alt="스크린샷 2023-12-19 232159" src="https://github.com/InseokJun/Hyundai-Softeer/assets/153903563/afb52e11-c650-4502-ad27-cd44de8e6581">

---
**Note**    
The provided statement suggests referring to the `Annual_Employee_Competition_Final_21_Truck_Solution.txt` file for detailed explanations and descriptions of the implemented code.
