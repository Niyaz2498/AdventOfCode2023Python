import typing
from src.utils.inputParser import convert_file_to_str_array
import os

# ip_list = convert_file_to_str_array(os.path.abspath('easy.txt'))
ip_list = convert_file_to_str_array(os.path.abspath('hard.txt'))

inst = ip_list[0]
inst_len = len(inst)
ip_len = len(ip_list)

ip_map: typing.Dict[str, typing.List[str]] = {}
for i in range(2, ip_len):
    key, val_str = ip_list[i].split(" = ")
    ip_map[key] = val_str[1:-1:].split(", ")

count, index, curr_pos = 0, 0, "AAA"
print(curr_pos)

while True:
    if index >= inst_len:
        index = 0
    if inst[index] == "L":
        curr_pos = ip_map[curr_pos][0]
    else:
        curr_pos = ip_map[curr_pos][1]

    count += 1
    print(curr_pos)
    if curr_pos == "ZZZ":
        break
    index += 1
print(count)
