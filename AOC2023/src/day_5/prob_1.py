from src.utils.inputParser import get_file_content_as_string
import typing
import os, pathlib, sys
from src.utils.day_5_commons import convert_section_to_map, get_val_from_map

ip_list = get_file_content_as_string(os.path.abspath('easy.txt')).split("\n\n")
# ip_list = get_file_content_as_string(os.path.abspath('hard.txt')).split("\n\n")

print(ip_list)
seed_list = ip_list[0].split(" ")
seed_list.pop(0)
# print(seed_list)

# convert to map
seed_to_soil_map = convert_section_to_map(ip_list, 1)
print("seed_to_soil_map")
print(seed_to_soil_map)
soil_to_fertilizer_map = convert_section_to_map(ip_list, 2)
print("soil_to_fertilizer")
print(soil_to_fertilizer_map)
fertilizer_to_water_map = convert_section_to_map(ip_list, 3)
print("fertilizer_to_water")
print(fertilizer_to_water_map)
water_to_light_map = convert_section_to_map(ip_list, 4)
print("water_to_light")
print(water_to_light_map)
light_to_temperature_map = convert_section_to_map(ip_list, 5)
print("light_to_temperature")
print(light_to_temperature_map)
temperature_to_humidity_map = convert_section_to_map(ip_list, 6)
print("temperature_to_humidity")
print(temperature_to_humidity_map)
humidity_to_location_map = convert_section_to_map(ip_list, 7)
print("humidity_to_location")
print(humidity_to_location_map)

close_locations = {}

least_close_location = sys.maxsize

for seed in seed_list:
    seed_num = int(seed)
    soil_num = get_val_from_map(seed_to_soil_map, seed_num)
    fert_num = get_val_from_map(soil_to_fertilizer_map, soil_num)
    water_num = get_val_from_map(fertilizer_to_water_map, fert_num)
    light_num = get_val_from_map(water_to_light_map, water_num)
    temp_num = get_val_from_map(light_to_temperature_map, light_num)
    humidity_num = get_val_from_map(temperature_to_humidity_map, temp_num)
    close_locations[seed_num] = get_val_from_map(humidity_to_location_map, humidity_num)
    if least_close_location >= close_locations[seed_num]:
        least_close_location = close_locations[seed_num]
    # close_locations[seed_num] = seed_to_soil_map.get(seed_num, seed_num)
print("\n---")
print(close_locations)
print("\n---")
print(least_close_location)
