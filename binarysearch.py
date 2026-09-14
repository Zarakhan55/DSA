# numbers = [10, 20, 30, 40, 50, 60, 70]

# target = 50

# low = 0
# high = len(numbers) - 1

# while low <= high:

#     mid = (low + high) // 2

#     if numbers[mid] == target:
#         print("Found:", target)
#         break

#     elif target > numbers[mid]:
#         low = mid + 1

#     else:
#         high = mid - 1



#2-task

# numbers = [10, 20, 30, 40, 50, 60, 70]

# target = 40

# low = 0
# high = len(numbers) - 1

# while low <= high:

#     mid = (low + high) // 2

#     if numbers[mid] == target:
#         print("Target Found:", target)
#         break

#     elif target > numbers[mid]:
#         low = mid + 1

#     else:
#         high = mid - 1
        
        
        
# roll_numbers = [101, 105, 110, 115, 120, 125, 130, 135, 140]
# target=130
# low=0
# high=len(roll_numbers)-1

# while low <= high:
#     mid=(low+high)//2
#     if roll_numbers[mid]==target:
#         print("Student found:",target)
#     elif target > roll_numbers[mid]:
#         low=mid+1
#     else:
#         high=mid-1


# task-4
# patient_ids = [1005, 1010, 1018, 1025, 1030, 1042, 1050, 1065, 1070]
# target=1042
# low=0
# high=len(patient_ids)-1

# while low <= high:
#     mid=(low+high)//2
#     if patient_ids[mid]==target:
#         print("Patient found:",target)
#     elif target > patient_ids[mid]:
#         low=mid+1
#     else:
#         high=mid-1



# task-5
account_numbers = [1001, 1008, 1015, 1022, 1030, 1045, 1052, 1060, 1075]
target = 1052
low=0
high=len(account_numbers)-1
while low <= high:
    mid=(low+high)//2
    if account_numbers[mid]==target:
        print("Account Number Found:",target)
        break
    elif target > account_numbers[mid]:
        low=mid+1
    else:
        high=mid-1
        