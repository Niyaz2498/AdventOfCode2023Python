import typing
from src.utils.inputParser import convert_file_to_str_array
from functools import reduce
import os


def reduce_to_next_row(seq: typing.List[int]) -> typing.Union[typing.List[int], None]:
    seq_len = len(seq)
    return_arr: typing.List[int] = []
    range_sum = 0
    for i in range(seq_len - 1):
        pair_diff = seq[i + 1] - seq[i]
        range_sum += pair_diff
        return_arr.append(pair_diff)
    print(return_arr)
    if range_sum == 0:
        return None
    return return_arr


def find_prev(seq: typing.List[int]):
    print(seq)
    first_elems: typing.List[int] = [seq[0]]
    while True:
        seq = reduce_to_next_row(seq)
        if seq is None:
            first_elems.reverse()
            return reduce(lambda a, b: b - a, first_elems)
        first_elems.append(seq[0])


# ip_list = convert_file_to_str_array(os.path.abspath('easy.txt'))
ip_list = convert_file_to_str_array(os.path.abspath('hard.txt'))
# print(ip_list)
sum = 0
for ip_elem in ip_list:
    sum += find_prev([int(x) for x in ip_elem.split()])
print(sum)
