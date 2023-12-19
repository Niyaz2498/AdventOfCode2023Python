import typing
from src.utils.inputParser import convert_file_to_str_array, convert_to_2d_array
import os

# ip_list = convert_file_to_str_array(os.path.abspath('easy.txt'))
ip_list = convert_file_to_str_array(os.path.abspath('hard.txt'))
ip_to_mat = convert_to_2d_array(ip_list)
row_count = len(ip_to_mat)
col_count = len(ip_to_mat[0])

# expand rows
i, count = 0, 0
while i < row_count:
    is_same: bool = True
    for curr_char in ip_to_mat[i]:
        if curr_char == '#':
            is_same = False
    if is_same:
        add_row = ip_to_mat[i].copy()
        ip_to_mat.insert(i, add_row)
        row_count += 1
        i += 1
    i += 1

# expand columns
j, count = 0, 0
while j < col_count:
    i = 0
    is_same: bool = True
    while i < row_count:
        if ip_to_mat[i][j] == '#':
            is_same = False
        i += 1
    i = 0
    if is_same:
        while i < row_count:
            ip_to_mat[i].insert(j, '.')
            i += 1
        j += 1
        col_count += 1
    j += 1

# list all galaxy

galaxy_list: typing.List[typing.List[int]] = []

for i in range(row_count):
    for j in range(col_count):
        if ip_to_mat[i][j] == "#":
            galaxy_list.append([i, j])

print(galaxy_list)
galaxy_count = len(galaxy_list)
diff_list: typing.List[int] = []
for i in range(galaxy_count - 1):
    for j in range(i + 1, galaxy_count):
        curr_node = galaxy_list[i]
        next_node = galaxy_list[j]
        diff = abs(next_node[0] - curr_node[0]) + abs(next_node[1] - curr_node[1])
        diff_list.append(diff)

print(diff_list)
print(sum(diff_list))
