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
    max = 0
    max_idx = -1
    for i, count in enumerate(read_elves(file_name)):
        if count > max:
            max = count
            max_idx = i

    print(max_idx, max)


def part_2_top_3_elf_calories(elves):
    all_elves = list(elves)
    all_elves.sort(reverse=True)
    print(sum(all_elves[:3]))


def main():
    file_name = 'input.txt'
    #part_1_elf_with_most_calories(read_elves(file_name))
    part_2_top_3_elf_calories(read_elves(file_name))


if __name__ == '__main__':
    main()

