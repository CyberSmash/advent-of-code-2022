def has_duplicates(elements):
    setOfElements = set()
    for element in elements:
        if element in setOfElements:
            return True
        else:
            setOfElements.add(element)
    return False

def main():
    with open("day6_input.txt", 'r') as fp:
        data = fp.read()

    marker_start = 0
    marker_end = marker_start + 4

    for marker_start in range(0, len(data)):
        if not has_duplicates(data[marker_start:marker_start+4]):
            print(f"start-of-packet marker started at {marker_start + 4}")
            break

    for marker_start in range(0, len(data)):
        if not has_duplicates(data[marker_start:marker_start+14]):
            print(f"start-of-message {marker_start + 14}")
            break



if __name__ == "__main__":
    main()