import sys

x = 1
cycle_num = 0
current_crt_row = list()
final_rows = list()
def do_cycle(instr, value=0):

    global x
    global cycle_num
    #print(f"{instr} - {value}  - Cycle: {cycle_num} X: {x}")

    while 1:
        if instr == "noop":
            cycle_num += 1
            #print(f"Cycle: {cycle_num} - {instr} - {value}  -  X: {x}")
            yield True
        elif instr == "addx":
            cycle_num += 1
            #print(f"Cycle: {cycle_num} - {instr} - {value}  -  X: {x}")
            yield False
            x += value
            cycle_num += 1
            #print(f"Cycle: {cycle_num} - {instr} - {value}  -  X: {x}")
            yield True
        else:
            print("Erorr: Unrecognized instruction. Exiting")
            sys.exit(1)


def print_sprite_position():
    global x
    sprite_draw_list = list(range(x - 1, x + 2))
    print("Sprite position: ", end='')
    for loc in range(0, 40):
        if loc in sprite_draw_list:
            print("#", end='')
        else:
            print('.', end='')
    print('')

def sprite_at_pos(pos):
    sprite_draw_list = list(range(x - 1, x + 2))
    return pos in sprite_draw_list
def print_pixel():
    pass

def cycle_callback(cycle_num, x, instr, value):
    global current_crt_row
    if cycle_num % 40 == 0:
        final_rows.append(''.join(current_crt_row))
        #for p in current_crt_row:
        #    print(p, end='')
        #print('')
        current_crt_row = list()
    if sprite_at_pos(cycle_num % 40):
        current_crt_row.append('#')
    else:
        current_crt_row.append('.')


    print(f"cycle : {cycle_num} - X: {x} - instr {instr} - value: {value}")
    print_sprite_position()
    print("Current CRT row: ", end='')
    for p in current_crt_row:
        print(p, end='')
    print('')
    print("")

def main():
    data = '''addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop'''


    with open("day10_input.txt", 'r') as fp:
        data = fp.read()

    global cycle_num
    global x
    instruction_lines = data.split('\n')
    strengths = list()
    next_strength_cycle = 20
    strength_cycle_step = 40


    #print_sprite_position()

    for instruction in instruction_lines:
        if instruction.startswith("noop"):


            cycle_callback(cycle_num, x, instruction, -1)
            cycle_num += 1
            if cycle_num == next_strength_cycle:
                strengths.append(x*cycle_num)
                next_strength_cycle += strength_cycle_step

        elif instruction.startswith("addx"):
            instr, value = instruction.split(' ')
            for num in range(0, 2):
                cycle_callback(cycle_num, x, instr, value)
                cycle_num += 1
                if cycle_num == next_strength_cycle:
                    strengths.append(x * cycle_num)
                    next_strength_cycle += strength_cycle_step

                if num == 1:
                    x += int(value)



    final_result = sum(strengths)
    print(f"Final Result: {final_result}")
    for final_row in final_rows:
        print(final_row)

    print(''.join(current_crt_row))


if __name__ == "__main__":
    main()