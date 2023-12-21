import typing
from src.utils.inputParser import convert_file_to_str_array, convert_to_2d_array
import os

# ip_list = convert_file_to_str_array(os.path.abspath('easy.txt'))
ip_list: typing.List[str] = convert_file_to_str_array(os.path.abspath('hard.txt'))

ip_to_mat: typing.List[typing.List[str]] = convert_to_2d_array(ip_list)
row_count = len(ip_to_mat)
col_count = len(ip_to_mat[0])
total_weight = 0

for i in range(col_count):
    col_weight = 0
    weightage = col_count
    for j in range(row_count):
        if ip_to_mat[j][i] == 'O':
            col_weight += weightage
            weightage -= 1
        elif ip_to_mat[j][i] == "#":
            weightage = col_count - j - 1
    total_weight += col_weight

print(total_weight)
