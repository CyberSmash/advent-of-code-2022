
def main():
    input = "CrZsJsPPZsGzwwsLwLmpwMDw"
    with open("day3_input.txt") as fp:
        data = fp.read()

    lines = data.split()
    total = 0

    for line in lines:
        part_a = set(line[:len(line) // 2])
        part_b = set(line[len(line) // 2:])

        common = list(part_a.intersection(part_b))[0]

        if 'A' <= common <= 'Z':
            val = ord(common) - 38
        else:
            val = ord(common) - ord('`')
        total += val
        #print(f"Common: {common}, Value: {val}")

    print(f"Final total: {total}")


if __name__ == "__main__":
    main()