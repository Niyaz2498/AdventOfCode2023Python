"""
The solution took 20 seconds for Hard.

TODO: Optimize if possible

"""
from src.utils.inputParser import convert_file_to_str_array
import os

# ip_list = convert_file_to_str_array(os.path.abspath('easy.txt'))
ip_list = convert_file_to_str_array(os.path.abspath('hard.txt'))
time_list = ip_list[0].split()
time_list.pop(0)
time_list = ["".join(time_list)]
speed_list = ip_list[1].split()
speed_list.pop(0)
speed_list = ["".join(speed_list)]

ip_map = {}
l = len(time_list)
ans = 1
for i in range(l):
    ways = 0
    tot_dut = int(time_list[i])
    print(tot_dut)
    tar_speed = int(speed_list[i])
    for j in range(tot_dut):
        print(j, end = " --> ")
        max_speed = j * (tot_dut - j)
        print (max_speed)
        if max_speed > tar_speed:
            break
        ways +=1
    print("====")
    print(ways)
    ways *= 2
    ways = tot_dut - ways + 1
    ans *= ways
    print("===")
print(ans)
