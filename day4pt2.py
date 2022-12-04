
def main() -> None:
    data = [
        "2-4,6-8",
        "2-3,4-5",
        "5-7,7-9",
        "2-8,3-7",
        "6-6,4-6",
        "2-6,4-8",
    ]

    with open("day4_input.txt", "r") as fp:
        input_data = fp.read()

    data = input_data.split("\n")

    final_pairs = list()
    for d in data:
        pairs = d.split(',')
        final_pairs.append(list())
        for p in pairs:
            elf_range = p.split('-')
            set_a = list(range(int(elf_range[0]), int(elf_range[1])+1))
            final_pairs[-1].append(set(set_a))

    print(final_pairs)

    #for pair in final_pairs:
    #    print(pair)
    count = 0
    for pair in final_pairs:
        #if pair[0].issubset(pair[1]) or pair[1].issubset(pair[0]):
        if not pair[0].isdisjoint(pair[1]):
            print(f"Pair: {pair} overlaps.")
            count += 1

    print(f"Final count: {count}")
if __name__ == "__main__":
    main()