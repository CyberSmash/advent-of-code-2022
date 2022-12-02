import sys
strategy = {"A": "rock",
            "B": "paper",
            "C": "scissors",
            "X": "rock",
            "Y": "paper",
            "Z": "scissors",
            }

shape_score = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}

rules = {
    "rock": {
        "beats": "scissors",
        "loses": "paper",
    },
    "paper": {
        "beats": "rock",
        "loses": "scissors",
    },
    "scissors": {
        "beats": "paper",
        "loses": "rock",
    }
}

WIN_POINTS = 6
DRAW_POINTS = 3
LOSS_POINTS = 0


def main():
    with open('day2_input.txt', 'r') as fp:
        data = fp.read()

    lines = data.split('\n')
    final_lines = list()
    for line in lines:
        final_lines.append(line.split())

    print(final_lines)
    #test_input = [('A', 'Y'), ('B', 'X'), ('C', 'Z')]

    my_score = 0
    for elf_play, my_play in final_lines:
        decoded_elf_play = strategy[elf_play]
        decoded_my_play = strategy[my_play]
        #print(f"{decoded_elf_play} vs. {decoded_my_play}")
        if decoded_elf_play == decoded_my_play:
            # Draw
            #print("We draw.")
            my_score += DRAW_POINTS + shape_score[decoded_my_play]

        elif rules[decoded_elf_play]["beats"] == decoded_my_play:
            # Loss
            #print("Elf wins.")
            my_score += LOSS_POINTS + shape_score[decoded_my_play]

        elif rules[decoded_elf_play]["loses"] == decoded_my_play:
            # Win
            #print("Elf Loses.")
            my_score += WIN_POINTS + shape_score[decoded_my_play]
        else:
            print("There was an error!!!")
            break
    print(f"My Score {my_score}")


if __name__ == "__main__":
    main()