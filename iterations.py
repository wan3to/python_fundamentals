# Итериране
squares = {1: 1, 2: 4, 3: 9}

for key in squares.keys():
    print(key, end=" ")

for value in squares.values():
    print(value, end=" ")

for key, value in squares.items():
    print(f"Key: {key}, Value: {value}")
