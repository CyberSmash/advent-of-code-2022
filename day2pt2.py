ROCK = 0
PAPER = 1
SCISSORS = 2

strategy = {"A": ROCK,
            "B": PAPER,
            "C": SCISSORS,
            }

OUTCOME_WIN = 0
OUTCOME_LOSE = 1
OUTCOME_DRAW = 2

outcome_table = {
    'X': OUTCOME_LOSE,
    'Y': OUTCOME_DRAW,
    'Z': OUTCOME_WIN,
}

shape_score = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
}

rules = {
    ROCK: {
        "beats": SCISSORS,
        "loses": PAPER,
    },
    PAPER: {
        "beats": ROCK,
        "loses": SCISSORS,
    },
    SCISSORS: {
        "beats": PAPER,
        "loses": ROCK,
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

    my_score = 0
    for elf_play, outcome in final_lines:

        decoded_elf_play = strategy[elf_play]
        decoded_outcome = outcome_table[outcome]

        if decoded_outcome == OUTCOME_DRAW:
            my_score += DRAW_POINTS + shape_score[decoded_elf_play]

        elif decoded_outcome == OUTCOME_LOSE:
            my_play = rules[decoded_elf_play]["beats"]
            my_score += LOSS_POINTS + shape_score[my_play]

        elif decoded_outcome == OUTCOME_WIN:
            my_play = rules[decoded_elf_play]["loses"]
            my_score += WIN_POINTS + shape_score[my_play]

    print(f"My Score {my_score}")
    

if __name__ == "__main__":
    main()