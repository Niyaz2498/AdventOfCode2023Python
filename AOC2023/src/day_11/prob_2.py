import typing
from src.utils.inputParser import convert_file_to_str_array, convert_to_2d_array
import os

# ip_list = convert_file_to_str_array(os.path.abspath('easy.txt'))
ip_list: typing.List[str] = convert_file_to_str_array(os.path.abspath('hard.txt'))
ip_to_mat: typing.List[typing.List[str]] = convert_to_2d_array(ip_list)
row_count = len(ip_to_mat)
col_count = len(ip_to_mat[0])

# this is to avoid inserting 1 million row or column
coordinate_distance_matrix: typing.List[typing.List[typing.List[int]]] = []

for i in range(row_count):
    temp_row: typing.List[typing.List[int]] = []
    for j in range(col_count):
        temp_row.append([i, j])
    coordinate_distance_matrix.append(temp_row)

# expand rows
i, count = 0, 0
for i in range(row_count):
    is_same: bool = True
    j = 0
    for j in range(col_count):
        if ip_to_mat[i][j] == '#':
            is_same = False
            coordinate_distance_matrix[i][j][0] += ((count))

    if is_same:
        count += 999999

# expand columns
j, count = 0, 0
while j < col_count:
    i = 0
    is_same: bool = True
    while i < row_count:
        if ip_to_mat[i][j] == '#':
            is_same = False
            coordinate_distance_matrix[i][j][1] += ((count))
        i += 1
    i = 0
    if is_same:
        count += 999999
    j += 1

for i in coordinate_distance_matrix:
    print(i)

for i in ip_to_mat:
    print(i)

# list all galaxy

galaxy_list: typing.List[typing.List[int]] = []

for i in range(row_count):
    for j in range(col_count):
        if ip_to_mat[i][j] == "#":
            galaxy_list.append([coordinate_distance_matrix[i][j][0], coordinate_distance_matrix[i][j][1]])

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
