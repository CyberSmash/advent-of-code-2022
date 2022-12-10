from rich import print
from typing import List



def calc_scenic_score(grid: List[List[int]], row: int, col: int) -> int:
    current_height = grid[row][col]

    scenic_score = 1
    # Look up
    distance = 0
    for row2 in range(row - 1, -1, -1):
        distance = row - row2

        if grid[row2][col] >= current_height:
            scenic_score *= distance
            break
    else:
        scenic_score *= distance

    # Look down

    for row2 in range(row + 1, len(grid)):
        distance = row2 - row

        if grid[row2][col] >= current_height:
            scenic_score *= distance
            break
    else:
        scenic_score *= distance

    # Look left
    visible = True
    for col2 in range(col - 1, -1, -1):
        distance = col - col2

        if grid[row][col2] >= current_height:
            scenic_score *= distance
            break
    else:
        scenic_score *= distance
    # Look right:

    for col2 in range(col + 1, len(grid[0])):
        distance = col2 - col

        if grid[row][col2] >= current_height:
            scenic_score *= distance
            break
    else:
        scenic_score *= distance
    return scenic_score

def is_visible(grid: List[List[int]], row: int, col: int):
    current_height = grid[row][col]


    visible = True
    # Look up
    for row2 in range(row - 1, -1, -1):
        if grid[row2][col] >= current_height:
            visible = False
            break

    if visible:
        return True

    # Look down
    visible = True
    for row2 in range(row + 1, len(grid)):
        if grid[row2][col] >= current_height:
            visible = False
            break
    if visible:
        return True

    # Look left
    visible = True
    for col2 in range(col - 1, -1, -1):
        if grid[row][col2] >= current_height:
            visible = False
            break

    if visible:
        return True

    # Look right:
    visible = True
    for col2 in range(col + 1, len(grid[0])):
        if grid[row][col2] >= current_height:
            visible = False
            break
    if visible:
        return True

    return False

def grid_perimeter(grid: List[List[int]]) -> int:
    if len(grid) != len(grid[0]):
        print("Error: The grid is not a square")

    return (2*len(grid)) + 2*(len(grid) - 2)

def get_grid(data: str) -> List[List[int]]:
    data_lines = data.split('\n')
    data_grid = [list(c) for c in data_lines]

    for r in range(len(data_grid)):
        for c in range(len(data_grid[0])):
            data_grid[r][c] = int(data_grid[r][c])

    return data_grid
def main():
    data = '''30373
25512
65332
33549
35390'''

    with open("day8_input.txt", "r") as fp:
        data = fp.read()

    data_grid = get_grid(data)
    perim_count = grid_perimeter(data_grid)
    print(data_grid)
    scenic_scores = dict()
    visible_count = perim_count

    for r in range(1, len(data_grid) - 1):
        for c in range(1, len(data_grid[r]) - 1):
            #if is_visible(data_grid, r, c):
            #    print(f"{data_grid[r][c]} ({r},{c}) is visible.")
            #    perim_count += 1

            scenic_score = calc_scenic_score(data_grid, r, c)
            scenic_scores[f"{r},{c}"] = scenic_score
            print(f"({r},{c}) = {scenic_score}")

    print(f"Max scenic score: {max(scenic_scores.values())}")

    print(f"Perim Count: {perim_count}")

if __name__ == "__main__":
    main()