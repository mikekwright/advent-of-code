from itertools import tee, islice
from functools import reduce
from typing import Sequence

LOWER_PRIORITY_START = 1
UPPER_PRIORITY_START = 27

def convert_item_to_priority(sack_item: str) -> int:
    if len(sack_item) > 1 or len(sack_item) <= 0:
        raise Exception("Unable to handle a sack item that isn't a single item")

    if sack_item.lower() == sack_item:
        return (ord(sack_item) - ord('a')) + LOWER_PRIORITY_START
    else:
        return (ord(sack_item) - ord('A')) + UPPER_PRIORITY_START

def find_sack_common_item(sack: str) -> str:
    sack_size = len(sack)
    half_size = sack_size // 2
    first_half = set(sack[:half_size])
    second_half = set(sack[half_size:])

    common_items_in_sac = first_half & second_half
    return common_items_in_sac.pop()

def find_group_common_item(sack_group: Sequence[str]) -> str:
    common_item = reduce(lambda l, r: l & r, (set(s) for s in sack_group))
    return common_item.pop()

def split_sacks_into_groups(sacks: Sequence[str]) -> enumerate[list[str]]:
    while True:
        next_group = list(islice(sacks, 3))
        if not next_group:
            break

        yield next_group

def load_sacks(file_name: str) -> enumerate[str]:
    with open(file_name, 'r') as f:
        for line in f:
            yield line.strip()

def main():
    file_name = 'input.txt'
    sacks = load_sacks(file_name)

    part1_sacks, part2_sacks = tee(sacks)

    priority_sum = sum(convert_item_to_priority(find_sack_common_item(sack)) for sack in part1_sacks)
    print(f'Part 1 - The priority of rucksacks: {priority_sum}')

    group_sum = sum(convert_item_to_priority(find_group_common_item(sack_group))
        for sack_group in split_sacks_into_groups(part2_sacks))
    print(f'Part 2 - The priority of groups: {group_sum}')

    #group_priority = sum(convert_item_to_priority(find_common_group(group) for 


if __name__ == '__main__':
    main()

