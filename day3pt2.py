def get_value(common_char):
    if 'A' <= common_char <= 'Z':
        return ord(common_char) - 38
    else:
        return ord(common_char) - ord('`')
def main():

    elf_a = set("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn")
    elf_b = set("ttgJtRGJQctTZtZT")
    elf_c = set("CrZsJsPPZsGzwwsLwLmpwMDw")

    ab = elf_a.intersection(elf_b)
    final = ab.intersection(elf_c)

    print(final)

    with open("day3_input.txt") as fp:
        data = fp.read()


    lines = data.split()
    total = 0
    for x in range(0, len(lines), 3):
        elf_a = set(lines[x])
        elf_b = set(lines[x+1])
        elf_c = set(lines[x + 2])

        ab = elf_a.intersection(elf_b)
        final = ab.intersection(elf_c)

        common_char = list(final)[0]

        total += get_value(common_char)

    print(total)

if __name__ == "__main__":
    main()