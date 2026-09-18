# numbers = [5, 2, 8, 3]

# for i in range(1, len(numbers)):

#     key = numbers[i]

#     j = i - 1

#     while j >= 0 and numbers[j] > key:

#         numbers[j + 1] = numbers[j]

#         j = j - 1

#     numbers[j + 1] = key

# print(numbers)


prices = [800, 300, 1200, 500, 200]
for x in range(1,len(prices)):
    key=prices[x]
    y=x-1
    while y>=0 and prices[y]>key:
        prices[y+1]=prices[y]
        y=y-1
    prices[y+1]=key
print(prices)