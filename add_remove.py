# Добавяне / махане
my_list = [1, 2, 3]
my_list.append(4)                   # [1, 2, 3, 4]
my_list.extend([5, 6])              # [1, 2, 3, 4, 5, 6]
my_list.insert(1, 100)              # [1, 100, 2, 3, 4, 5, 6]

my_list.remove(100)                 # по стойност
number = my_list.pop(0)             # по индекс, връща елемента
my_list.clear()                     # []
