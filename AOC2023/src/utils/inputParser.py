import typing


def convert_to_2d_array(ip_str_arr: typing.List[str]):
    return [[char for char in ip_str] for ip_str in ip_str_arr]


# this converts the string input in file and converts it to list of string where each line is a  string.
def convert_file_to_str_array(filename: str) -> typing.List[str]:
    return [line.rstrip() for line in open(filename)]
