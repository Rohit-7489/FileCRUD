# BUBBLE SORT IN LIST


# a = [56,12,89,23,56,90,13]

# for j in range(len(a)-1):
#     for i in range(0,len(a)-1-j):
#         if a[i] > a [i+1]:
#             a[i],a[i+1] = a[i+1],a[i]
        

# print(a)

# Q-44

a = [12,56,23,56,23,45,76,56,342,23,12,34,5]
largest = a[0]
index = 0

for i in range(1,len(a)):
    if a[i] > largest:
        largest = a[i]
        index = i
print(f"largest element is {largest} at index {index}")

find 2