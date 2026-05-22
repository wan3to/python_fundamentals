# Допълнителни методи
my_list = [1, 2, 3, 2, 2]
my_list.count(2)          # 3
pos = my_list.index(2)    # 1
my_list.reverse()         # [2, 2, 3, 2, 1]

# Размяна на елементи
nums = [1, 2, 3]
nums[0], nums[1], nums[2] = nums[2], nums[0], nums[1]
# [3, 1, 2]

# Слепване на листове
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
final_list = nums1 + nums2           # [1, 2, 3, 4, 5, 6]

# Уникални елементи
numbers = [1, 2, 2, 3, 1, 4, 5, 4]
unique_numbers = list(set(numbers))  # [1, 2, 3, 4, 5]
