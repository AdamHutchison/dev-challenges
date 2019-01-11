### Challenge 1 - Fibonacci staircase

#### Task:
A child is running up a staircase with n steps and can hop either 1 step, 2 steps or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.

#### Example:
If there were 4 steps (i.e. `n = 4`), there would be 7 ways that the child could go up the steps:

```
1-1-1-1
2-1-1
1-2-1
1-1-2
2-2
3-1
1-3
```

Your method needs to return 7 in this situation.

#### Hints:
* Use memoisation to avoid quickly overflowing the stack.
* Recursion could be used to solve this