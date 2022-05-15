## Bit Operations
1. For n >= 0, it takes at least `ceil(log2(n+1))` to represent it:
```
There are in total n+1 numbers from 0 to n and m bits can 
represent 2 ** m numbers. 

So to represent n+1 numbers, we need 2 ** m >= n + 1 -> m >= log_2(n+1) -> 
minimum m = ceil(log_2(n+1))
```

2. Bitwise-or will always result in a greater or equal result:
```
bitwise-or operation can only turn a 0 bit into 1 or 0.
```