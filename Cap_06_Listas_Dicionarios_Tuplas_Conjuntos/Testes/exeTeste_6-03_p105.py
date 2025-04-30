# Data: 24/04/2025

# ============ EXERCÍCIO 6.03 (PÁG. 105) ============

# Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.

list1 = [1, 2, 3, 4, 5]
# list1 = [1, 4, 5, 6, 7]
list2 = [4, 5, 6, 7, 8, 9]
list3 = list1
count_l2 = 0
idx_num_repetido_l2 = []
while count_l2 < len(list2):
    idx_l1 = 0
    while idx_l1 < len(list1):
        if list1[idx_l1] == list2[count_l2]:
            idx_num_repetido_l2.append(count_l2)
        idx_l1 += 1
    count_l2 += 1
# print(idx_num_repetido_l2)
# print(len(idx_num_repetido_l2))
count = 0
position = 0
while count < len(list2):
    if count != position:
        list3.append(list2[count])
    count += 1
    if position < len(idx_num_repetido_l2):
        position += 1
# print(position)
print(list3)
