# List comprehensions – шаблон
x = [num for num in range(5)]                # [0, 1, 2, 3, 4]
nums = [1, 2, 3, 4]
squares = [x**2 for x in nums]               # [1, 4, 9, 16]

# с if / if-else
nums = [1, 2, 3, 4, 5, 6]
evens = [n for n in nums if n % 2 == 0]      # [2, 4, 6]
filtered = [True if x % 2 == 0 else False for x in nums]
