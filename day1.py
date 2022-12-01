
def main():
    elves = []
    with open("./day1_input.txt") as fp:
        lines = fp.readlines()

    elves.append(0)
    for line in lines:
        if line == '\n':
            elves.append(0)
            continue
        stripped_line = line.rstrip()
        calories = int(stripped_line)
        elves[-1] += calories


    # Answer to part 1:
    print(f"Biggest value: {max(elves)}")

    # Answer to part 2:
    elves.sort(reverse=True)
    print(f"The biggest three values summed value: {sum(elves[:3])}")

if __name__ == '__main__':
    main()


