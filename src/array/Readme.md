## Bit Operations
1. For n >= 0, it takes `ceil(log2(n+1))` to represent it:
```
There are in total n+1 numbers from 0 to n. m bits can 
represent 2 ** m numbers. 

So to represent n+1 numbers, we need 2 ** m >= n + 1 -> m >= log_2(n+1) -> 
m = ceil(log_2(n+1))
```