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

def load_sacks(file_name: str) -> enumerate[str]:
    with open(file_name, 'r') as f:
        for line in f:
            yield line.strip()

def main():
    file_name = 'input.txt'
    sacks = load_sacks(file_name)

    priority_sum = sum(convert_item_to_priority(find_sack_common_item(sack)) for sack in sacks)
    print(f'Part 1 - The priority of rucksacks: {priority_sum}')


if __name__ == '__main__':
    main()

