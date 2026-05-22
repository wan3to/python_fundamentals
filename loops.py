# for с range()
for x in range(3):
    print(x)    # 0, 1, 2

# Обхождане на стринг отзад напред
word = input()
reversed_word = ""
for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]
print(reversed_word)
