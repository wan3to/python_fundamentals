# Логически оператори
if a > b and c > a: # type: ignore
    print("Both conditions are True")

if a > b or a > c: # pyright: ignore[reportUndefinedVariable]
    print("At least one is True")

if not a > c: # type: ignore
    print("Condition is False")

# Проверка дали число е в интервал
a = int(input())
if 1 <= a <= 10:
    print("a is in the range 1 and 10")
