# Примери от задачи
# Courses
n = int(input())
courses = []
for _ in range(n):
    courses.append(input())
print(courses)

# List Statistics
n = int(input())
positives = []
negatives = []
for _ in range(n):
    num = int(input())
    if num >= 0:
        positives.append(num)
    else:
        negatives.append(num)
print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {sum(negatives)}")
