# Итерация през лист
my_list = ["dog", "cat", "fish"]

for element in my_list:
    print(element, end=" ")

for i in range(len(my_list)):
    print(my_list[i], end=" ")

# while
i = 0
while i < len(my_list):
    print(my_list[i], end=" ")
    i += 1
