# Truck Size Decision for Maximum Revenue

## Problem Overview
As a truck designer for Hyundai Motor Group, you are tasked with determining the size of a new truck. To make an informed decision, you've surveyed a total of N consumers, each providing multiple purchase proposals based on the truck's size.

Each consumer i (1 ≤ i ≤ N) has submitted Ai proposals. Proposal j (1 ≤ j ≤ Ai) from consumer i states, "I am willing to purchase a truck at a price of Pi,j won if the size is greater than or equal to Si,j."

However, accommodating a customized truck for each consumer incurs significant facility costs. Therefore, you need to decide on a single truck size that satisfies various consumer proposals.

Since consumers won't purchase more than two trucks, you will either accept one proposal from each consumer or reject all proposals. The chosen truck size should maximize the total revenue.

To explore revenue scenarios, you plan to consider M scenarios. For each scenario k (1 ≤ k ≤ M), you need to find the minimum truck size to achieve a total revenue of at least Qk won.

## Constraints
1 ≤ N ≤ 100,000
For all i, j (1 ≤ i ≤ N, 1 ≤ j ≤ Ai), 1 ≤ Si,j, Pi,j ≤ 10^9
1 ≤ M ≤ 100,000
For all k (1 ≤ k ≤ M), 1 ≤ Qk ≤ 10^9


## Input Format
First line: N (total number of consumers)
Next N lines: Consumer proposals
Format for each line i (1 ≤ i ≤ N): Ai Si,1 Pi,1 … Si,Ai Pi,Ai
Next line: M (number of scenarios)
Last line: M integers representing Q1, Q2, …, QM

## Output Format
M integers separated by a single space.
If it's possible to achieve Qk won or more in revenue, output the minimum truck size.
If it's not possible, output -1.

### Example Input 1
```
4
1 1 1
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
