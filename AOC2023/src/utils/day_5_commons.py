import typing


def convert_section_to_map(list_ip: typing.List[str], index: int) -> typing.Dict[typing.Tuple[int, int], int]:
    a_to_b_list = list_ip[index].split("\n")
    a_to_b_list.pop(0)
    # print(a_to_b_list)
    a_to_b_map = {}
    for i in a_to_b_list:
        destination_start, source_start, range_len = i.split(" ")
        src_tuple = (int(source_start), int(source_start) + int(range_len) - 1)
        a_to_b_map[src_tuple] = int(destination_start)
    return a_to_b_map


def get_val_from_map(ip_map: typing.Dict[typing.Tuple[int, int], int], val: int) -> int:
    for i in ip_map:
        # if val between values of  tuple
        if i[0] <= val <= i[1]:
            return ip_map[i] + (val - i[0])
    return val
