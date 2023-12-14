"""

TODO: variable names needs refactoring

"""
import typing

from src.utils.inputParser import convert_file_to_str_array
from functools import cmp_to_key
import os


def compare(item1, item2):
    val_map: typing.Dict[str, int] = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'J': 11,
        'T': 10
    }
    for ip in range(5):
        val1 = item1[0][ip]
        val2 = item2[0][ip]
        val1 = int(val1) if val1 not in val_map else val_map[val1]
        val2 = int(val2) if val2 not in val_map else val_map[val2]
        if val1 > val2:
            return -1
        elif val1 < val2:
            return 1


def get_category(ip_str: str) -> int:
    char_map: typing.Dict[str, int] = {}
    for pos in ip_str:
        if pos in char_map:
            char_map[pos] += 1
        else:
            char_map[pos] = 1
    # Five of a kind
    if len(char_map) == 1:
        return 7

    if len(char_map) == 2:
        for char in char_map:
            # Four of a kind
            if char_map[char] == 4:
                return 6

        # Full House
        return 5

    if len(char_map) == 3:
        for char in char_map:
            # Three of a kind
            if char_map[char] == 3:
                return 4

        # Two pair
        return 3

    # One pair
    if len(char_map) == 4:
        return 2

    # High card
    if len(char_map) == 5:
        return 1


# ip_list = convert_file_to_str_array(os.path.abspath('easy.txt'))
ip_list = convert_file_to_str_array(os.path.abspath('hard.txt'))

print(ip_list)
ip_len = len(ip_list)
segregated_card_map: typing.Dict[int, typing.List[typing.Tuple[str, int]]] = {}
for ip in ip_list:
    card, bid = ip.split()
    card_bid_pair: typing.Tuple[str, int] = (card, int(bid))
    category = get_category(card)
    if category in segregated_card_map:
        segregated_card_map[category].append(card_bid_pair)
    else:
        cat_value = [card_bid_pair]
        segregated_card_map[category] = cat_value
print(segregated_card_map)

ans: int = 0
for i in range(7, 0, -1):
    # print(i)
    if i not in segregated_card_map:
        continue
    for pair in sorted(segregated_card_map[i], key=cmp_to_key(compare)):
        print(pair)
        ans += pair[1] * ip_len
        ip_len -= 1

print(ans)
