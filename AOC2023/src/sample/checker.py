from src.utils.inputParser import convert_file_to_str_array, convert_to_2d_array
import  os, pathlib
# print(os.path.abspath('easy.txt'))
ip_to_line = convert_file_to_str_array(os.path.abspath('easy.txt'))
print(ip_to_line)

# print(convert_to_2d_array(ip_to_line))