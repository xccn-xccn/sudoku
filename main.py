from time import perf_counter


def search(puzzle):
    for y, line in enumerate(puzzle):
        for x, num in enumerate(line):
            if num == 0:
                return [y, x, 0]


def remove_zero(alist):
    return [x for x in alist if x != 0]


def valid(y, x, puzzle, section):
    value = puzzle[y][x]
    line, column = remove_zero(puzzle[y]), remove_zero(
        [line[x] for line in puzzle])
    return True if len(line) == len(set(line)) and len(column) == len(set(column)) and value not in section else False


def begin(puzzle):
    mutable = []
    sections = [[] for _ in range(9)]
    if len(puzzle) != 9:
        return False
    for y, line in enumerate(puzzle):
        if len(puzzle) != 9:
            return False
        for x, num in enumerate(line):
            if num > 9 or num < 0 or (num != 0 and not valid(y, x, puzzle, [[]] * 9)):
                raise Exception
            else:
                if num == 0:
                    mutable.append((y, x))
                else:
                    sections[x//3 + (y//3)*3].append(num)
    return mutable, sections


def solve_single(puzzle, seen=None):
    print(puzzle)
    # TODO make it error on multiple solutions and refactor code is too slow on 17 hint puzzles ?
    # make able checker better using valid
    # change sections make each item in possible have its own puzzle (board)
    # also got to ensure no repeats (set of tuple)

    if seen == None:
        seen = set()
    mutable, sections = begin(puzzle)
    print(mutable)
    count = 0
    success = False
    mutable_sections = [[] for x in range(9)]
    # possible = [0]  #stores the index of mutable
    index = 0
    multiple_solutions = False
    seen = set()
    while True:  # needs to change
        y, x = mutable[index]
        # print(y, x, sections)
        sections_index = x//3 + (y//3)*3
        success = False
        if puzzle[y][x] == 0:
            new = True
        else:
            sections[sections_index].pop()
        # print(puzzle[y][x], "should be 0")
        while success == False and puzzle[y][x] < 9:
            puzzle[y][x] += 1
            success = valid(y, x, puzzle, sections[sections_index])
        # print(success, puzzle[y][x])
        if success:
            sections[sections_index].append(puzzle[y][x])
            index += 1
            if index == len(mutable):
                return puzzle
        else:
            index -= 1
            if index < 0:  # is negative indexing
                break
            # if not new:
            #     sections[sections_index].pop()
            puzzle[y][x] = 0
    return "FAIL"


def sudoku_solver(puzzle):
    mutable, sections = begin(puzzle)


if __name__ == "__main__":
    start = perf_counter()
    print(solve_single([[8, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 3, 6, 0, 0, 0, 0, 0], 
[0, 7, 0, 0, 9, 0, 2, 0, 0], 
[0, 5, 0, 0, 0, 7, 0, 0, 0],
[0, 0, 0, 0, 4, 5, 7, 0, 0], 
[0, 0, 0, 1, 0, 0, 0, 3, 0],
[0, 0, 1, 0, 0, 0, 0, 6, 8], 
[0, 0, 8, 5, 0, 0, 0, 1, 0], 
[0, 9, 0, 0, 0, 0, 4, 0, 0]]))
    print(f"{(perf_counter() - start) * 1000}")
