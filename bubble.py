# numbers = [5, 2, 8, 1]

# for i in range(len(numbers)):
#     for j in range(0, len(numbers) - 1):

#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# print(numbers)

# prices = [1200, 500, 2500, 800, 1500]
# for a in range(len(prices)):
#     for b in range(0,len(prices)-a -1):
#         if prices[b]>prices[b+1]:
#             prices[b],prices[b+1]=prices[b+1],prices[b]
# print(prices)

marks = [72, 95, 64, 88, 51, 90]
for x in range(len(marks)):
    for y in range(len(marks)-1):
        if marks[y+1]>marks[y]:
            marks[y+1],marks[y]=marks[y],marks[y+1]
print(marks)