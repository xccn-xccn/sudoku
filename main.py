def search(puzzle):
    for y, line in enumerate(puzzle):
        for x, num in enumerate(line):
            if num == 0:
                return [y, x, 0]


def remove_zero(alist):
    return [x for x in alist if x != 0]


def valid(details, puzzle, section):
    y, x, attempt = details
    line, column = remove_zero(puzzle[y]), remove_zero([line[x] for line in puzzle])
    # print(line, column)
    return True if len(line) == len(set(line)) and len(column) == len(set(column)) and attempt not in section else False


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
            if num > 9 or num < 0 or (num != 0 and not valid((y, x, num), puzzle, [[]] * 9)):
                raise Exception
            else:
                mutable.append((y, x))
                sections[x//3 + (y//3)*3].append(num)
    return mutable


def sudoku_solver(puzzle):
    print(puzzle)
    # TODO make it error on multiple solutions and refactor code is too slow on 17 hint puzzles ?
    # make able checker better using valid
    # change sections make each item in possible have its own puzzle (board)
    #also got to ensure no repeats (set of tuple)

    mutable, sections = begin(puzzle)
    count = 0
    success = False
    mutable_sections = [[] for x in range(9)]
    possible = [(0, puzzle)]  #stores the index of mutable and the current puzzle
    index = 0
    multiple_solutions = False
    seen = set()
    while possible:
        count += 1
        print(count)
        # print(possible)
        index = possible.pop()
        y, x, current_puzzle = mutable[index]
        sections_index = x//3 + (y//3)*3
        while success == False and puzzle[y][x] < 9:
            puzzle[y][x] += 1
            # success = valid(puzzle[y][x], puzzle, fixed_sections[x//3 + (y//3)*3] + mutable_sections[x//3 + (y//3)*3])
            success = valid(puzzle[y][x], puzzle, sections[sections_index]) 
        if success:
            sections[sections_index].append(puzzle[y][x])
            index += 1
            if index == len(mutable):
                if multiple_solutions:
                    raise Exception
                else:
                    multiple_solutions = True
            else:
                possible.append(index)
        else:
            sections[sections_index].pop()
            y, x, poss = possible.pop()
            if puzzle[y][x] == sections[sections_index][-1]:
                sections[sections_index].pop()
            puzzle[y][x] = 0
        success = False
    raise Exception


if __name__ == "__main__":
    print(begin([[0, 9, 6, 5, 0, 4, 0, 7, 1],
                 [0, 2, 0, 1, 0, 0, 0, 0, 0],
                 [0, 1, 4, 0, 9, 0, 6, 2, 3],
                 [0, 0, 3, 0, 6, 0, 0, 8, 0],
                 [0, 0, 8, 0, 5, 0, 4, 0, 0],
                 [9, 0, 0, 4, 0, 0, 0, 0, 5],
                 [7, 0, 0, 0, 0, 9, 0, 0, 0],
                 [0, 0, 1, 0, 7, 5, 3, 4, 9],
                 [2, 3, 0, 0, 4, 8, 1, 0, 7]]))
