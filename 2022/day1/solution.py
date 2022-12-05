def main():
    file_name = 'input.txt'
    elves = []
    with open(file_name, 'r') as f:
        current_elf = 0
        while True:
            line = f.readline()
            if len(line) <= 0:
                break

            line = line.strip()
            if line == '':
                elves.append(current_elf)
                current_elf = 0
                continue

            calories = int(line)
            current_elf += calories

        if current_elf > 0:
            elves.append(current_elf)

    max = 0
    max_idx = -1
    for i, count in enumerate(elves):
        if count > max:
            max = count
            max_idx = i

    print(max_idx, max)


if __name__ == '__main__':
    main()

