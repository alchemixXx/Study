# list1 = [1,2,3]
# list2 = []
# for spacex in list1:
#     if spacex == 3:
#         continue
#     if spacex != 3:
#         list2.append(spacex)
# print(list1)

list1 = [1,2,3]
list2 = []
list2 = list2 + list1
list1.clear()
for spacex in list2:
    if spacex == 3:
        continue
    if spacex != 3:
        list1.append(spacex)
print(list1)

# for spacex in list1:
    # if spacex == 3:
    #     continue
    # if spacex != 3:
    #     list2.append(spacex)
# print(list2)