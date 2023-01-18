def search(puzzle):
    for y, line in enumerate(puzzle):
        for x, num in enumerate(line):
            if num == 0:
                return [y, x, 0]


def remove_zero(alist):
    return [x for x in alist if x != 0]


def valid(y, x, puzzle, section):
    value = puzzle[y][x]
    line, column = remove_zero(puzzle[y]), remove_zero([line[x] for line in puzzle])
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
            #print(y, x, num, valid((y, x, num), puzzle, [[]] * 9), "in begin")
            if num > 9 or num < 0 or (num != 0 and not valid(y, x, puzzle, [[]] * 9)):
                raise Exception
            else:
                mutable.append((y, x))
                sections[x//3 + (y//3)*3].append(num)
    return mutable, sections


def solve_single(puzzle, seen = None):
    print(puzzle)
    # TODO make it error on multiple solutions and refactor code is too slow on 17 hint puzzles ?
    # make able checker better using valid
    # change sections make each item in possible have its own puzzle (board)
    #also got to ensure no repeats (set of tuple)

    if seen == None:
        seen = set()
    mutable, sections = begin(puzzle)
    count = 0
    success = False
    mutable_sections = [[] for x in range(9)]
    #possible = [0]  #stores the index of mutable 
    index = 0
    multiple_solutions = False
    seen = set()
    while True: #needs to change
        count += 1
        print(count, index)
        y, x = mutable[index]
        sections_index = x//3 + (y//3)*3
        success = False
        new = puzzle[y][x] == 0
        while success == False and puzzle[y][x] < 9:
            puzzle[y][x] += 1
            success = valid(y, x, puzzle, sections[sections_index]) 
        if success:
            sections[sections_index].append(puzzle[y][x])
            index += 1
            if index == len(mutable):
                return puzzle
        else:
            index -= 1
            if index < 0:
                break
            if not new:
                sections[sections_index].pop()
            puzzle[y][x] = 0
    return puzzle 


def sudoku_solver(puzzle):
    mutable, sections = begin(puzzle)


if __name__ == "__main__":
    print(solve_single([[0, 9, 6, 5, 0, 4, 0, 7, 1],
                 [0, 2, 0, 1, 0, 0, 0, 0, 0],
                 [0, 1, 4, 0, 9, 0, 6, 2, 3],
                 [0, 0, 3, 0, 6, 0, 0, 8, 0],
                 [0, 0, 8, 0, 5, 0, 4, 0, 0],
                 [9, 0, 0, 4, 0, 0, 0, 0, 5],
                 [7, 0, 0, 0, 0, 9, 0, 0, 0],
                 [0, 0, 1, 0, 7, 5, 3, 4, 9],
                 [2, 3, 0, 0, 4, 8, 1, 0, 7]]))
