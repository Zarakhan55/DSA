# numbers = [6, 3, 8, 2, 7]

# for i in range(len(numbers)):

#     min_index = i

#     for j in range(i + 1, len(numbers)):

#         if numbers[j] < numbers[min_index]:
#             min_index = j

#     numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

# print(numbers)

prices = [900, 250, 1200, 450, 700]
for i in range(len(prices)):
    min_index=i
    for j in range(i+1,len(prices)):
        if prices[j]<prices[min_index]:
            min_index=j
    prices[i],prices[min_index]=prices[min_index],prices[i]
print(prices)