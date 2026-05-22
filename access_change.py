# Достъп и промяна
my_dict = {"name": "Jack", "age": 26}
print(my_dict["name"])          # Jack
print(my_dict.get("age"))       # 26
print(my_dict.get("address"))   # None

my_dict["age"] = 27             # update
my_dict["city"] = "Sofia"       # нов ключ
