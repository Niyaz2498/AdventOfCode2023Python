import typing
from src.utils.inputParser import convert_file_to_str_array, convert_to_2d_array
import os


def is_valid_coordinate(x: int, y: int, x_max, y_max):
    return 0 <= x < x_max and 0 <= y < y_max


def find_farthest(ip_to_mat: typing.List[typing.List[str]], x: int, y: int):
    curr_level_elems: typing.List[typing.List[int]] = [[x, y]]
    row_count = len(ip_to_mat)
    col_count = len(ip_to_mat[0])
    seen = set()
    level: int = -1
    while curr_level_elems:
        temp_elem = []
        for elem in curr_level_elems:
            key = str(elem[0]) + "-" + str(elem[1])
            curr_char = ip_to_mat[elem[0]][elem[1]]
            if key in seen:
                continue
            # left
            if curr_char == '-' or curr_char == '7' or curr_char == 'J' or curr_char == 'S':
                left_x = elem[0]
                left_y = elem[1] - 1
                if is_valid_coordinate(left_x, left_y, row_count, col_count):
                    left_elem = ip_to_mat[left_x][left_y]
                    if left_elem == '-' or left_elem == 'L' or left_elem == 'F':
                        temp_elem.append([left_x, left_y])
            # right
            if curr_char == '-' or curr_char == 'L' or curr_char == 'F' or curr_char == 'S':
                right_x = elem[0]
                right_y = elem[1] + 1
                if is_valid_coordinate(right_x, right_y, row_count, col_count):
                    right_elem = ip_to_mat[right_x][right_y]
                    if right_elem == '-' or right_elem == '7' or right_elem == 'J':
                        temp_elem.append([right_x, right_y])
            # up
            if curr_char == '|' or curr_char == 'L' or curr_char == 'J' or curr_char == 'S':
                up_x = elem[0] - 1
                up_y = elem[1]
                if is_valid_coordinate(up_x, up_y, row_count, col_count):
                    top_elem = ip_to_mat[up_x][up_y]
                    if top_elem == '|' or top_elem == '7' or top_elem == 'F':
                        temp_elem.append([up_x, up_y])
            # down
            if curr_char == '|' or curr_char == '7' or curr_char == 'F' or curr_char == 'S':
                down_x = elem[0] + 1
                down_y = elem[1]
                if is_valid_coordinate(down_x, down_y, row_count, col_count):
                    bottom_elem = ip_to_mat[down_x][down_y]
                    if bottom_elem == '|' or bottom_elem == 'L' or bottom_elem == 'J':
                        temp_elem.append([down_x, down_y])
            seen.add(key)
        if len(temp_elem) != 0:
            level += 1
            curr_level_elems = temp_elem
        else:
            break
    return level


# ip_list = convert_file_to_str_array(os.path.abspath('easy.txt'))
# ip_list = convert_file_to_str_array(os.path.abspath('easy_2.txt'))
ip_list = convert_file_to_str_array(os.path.abspath('hard.txt'))
ip_to_mat = convert_to_2d_array(ip_list)
print(ip_to_mat)
row_count = len(ip_to_mat)
col_count = len(ip_to_mat[0])
x, y = 0, 0
for i in range(row_count):
    flag = False
    for j in range(col_count):
        if ip_to_mat[i][j] == 'S':
            flag = True
            x, y = i, j
            break
    if flag:
        break
level = find_farthest(ip_to_mat, x, y)
print(level)

"""

['.', '.', '.', '.', '.']
['.', 'S', '-', '7', '.'] 
['.', '|', '.', '|', '.'] 
['.', 'L', '-', 'J', '.'] 
['.', '.', '.', '.', '.']


"""
