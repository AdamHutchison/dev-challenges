### Challenge 3 - Matrix Search

#### Task:
Given an M x N matrix (two dimentional array), in which each row and each column is sorted in ascending order, write a method to find an element. If the matrix contains dublicates then you only need to return the location of 1.

#### Example:
You have an array such as this `[a, b, c, d]` where each of the element `a`, `b`, `c`, `d` and `e` are themselves arrays.
The values of `a`, `b`, `c` and `d` are as follows:
`a = [1, 2, 3, 4]`
`b = [5, 6, 7, 8]`
`c = [9, 10, 11, 12]`
`d = [13, 14, 15, 16]`
`e = [13, 14, 15, 16]`

or all together:

```
[
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [13, 14, 15, 16],
]
```

In this situation `M = 5` and `N = 4`

If the number 10 was inputted to your method then is should return `[2, 1]` (in the format of `[M, N]`) as 10 is the second element in the third array (using the 0 based index).