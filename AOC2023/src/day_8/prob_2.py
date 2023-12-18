"""
Solved with a hint. Yet to understand why LCM works and what are the cases where LCM can be helpful

"""
import math
import typing
from src.utils.inputParser import convert_file_to_str_array
import os


def next_pos_list(ip_map: typing.Dict[str, typing.List[str]], curr_pos_list: typing.List[str], dir: str) -> typing.Union[typing.List[str], None]:
    return_list = []
    count = 0
    for pos in curr_pos_list:
        next_pos = ""
        if dir == "L":
            next_pos = ip_map[pos][0]
        else:
            next_pos = ip_map[pos][1]

        return_list.append(next_pos)
        if next_pos[-1] == 'Z':
            count += 1

    if len(return_list) == count:
        return None
    return return_list


# ip_list = convert_file_to_str_array(os.path.abspath('easy_2.txt'))
ip_list = convert_file_to_str_array(os.path.abspath('hard.txt'))

inst = ip_list[0]
inst_len = len(inst)
ip_len = len(ip_list)
ip_map: typing.Dict[str, typing.List[str]] = {}

for i in range(2, ip_len):
    key, val_str = ip_list[i].split(" = ")
    ip_map[key] = val_str[1:-1:].split(", ")

index = 0
pos_list: typing.List[str] = []
for key in ip_map:
    if key[-1] == 'A':
        pos_list.append(key)

count_list: typing.List[int] = []
for temp in pos_list:
    temp_list = [temp]
    count = 0
    while temp_list:
        if index >= inst_len:
            index = 0
        temp_list = next_pos_list(ip_map, temp_list, inst[index])
        count += 1
        index += 1
    count_list.append(count)

print(count_list)
print(math.lcm(*count_list))
