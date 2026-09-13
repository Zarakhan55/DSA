# marks = [75, 90, 65, 88, 95]
# highest=marks[0]
# for mark in marks:
#     if mark>highest:
#         highest=mark
# print("HIgest mark:",highest)


numbers = [12, 7, 20, 15, 8, 3, 10]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
