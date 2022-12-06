def read_elves(file_name):
    with open(file_name, 'r') as f:
        current_elf = 0
        while True:
            line = f.readline()
            if len(line) <= 0:
                break

            line = line.strip()
            if line == '':
                yield current_elf
                current_elf = 0
                continue

            calories = int(line)
            current_elf += calories

        if current_elf > 0:
            yield current_elf


def part_1_elf_with_most_calories(elves):
    print(f'Maximum calories for a single elf: {max(elves)}')


def part_2_top_3_elf_calories(elves):
    elves.sort(reverse=True)
    print(f'Maximum calories for top 3 elves: {sum(elves[:3])}')


def main():
    file_name = 'input.txt'
    all_elves = list(read_elves(file_name))
    part_1_elf_with_most_calories(list(all_elves))
    part_2_top_3_elf_calories(list(all_elves))


if __name__ == '__main__':
    main()

