import hashlib

def find_the_santa_mine(input: str, count: int = 5, start_num: int = 0) -> int:
    num = start_num
    encoded = input.encode()
    itr = 0

    sequence = '0' * count
    while True:
        if itr % 100000 == 0:
            print('.', end='', flush=True)
        itr += 1

        hash = hashlib.md5(encoded + str(num).encode()).hexdigest()
        if hash[:count] == sequence:
            print()
            return num

        num += 1
