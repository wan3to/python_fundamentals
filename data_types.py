# Основни типове
int_num = 10             # int
float_num = 10.2         # float
a_str = "Hello"          # str
is_true = True           # bool

# Проверка на типа
print(type("123"))       # <class 'str'>
print(type(123))         # <class 'int'>
print(isinstance("123", str))  # True

# Преобразуване на типове
x = int("5")             # 5
y = float("3.14")        # 3.14
s = str(3.5)             # "3.5"

a = 5
b = 10

# Булеви изрази и сравнения
print(a == b)       # равно
print(a != b)       # различно
print(a < b)        # по-малко
print(a <= b)       # по-малко или равно
print(a > b)        # по-голямо
print(a >= b)       # по-голямо или равно
