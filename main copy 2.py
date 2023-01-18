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
    sections = []
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
    # change sections

    mutable, fixed_sections = begin(puzzle)
    count = 0
    success = False
    mutable_sections = [[] for x in range(9)]
    possible = [0] #stores the index of mutable
    index = 0
    # gets the numbers in the 3x3 area add a muttable coordinates (if it is 0)
    # for y, line in enumerate(puzzle):
    #     for x, num in enumerate(line):
    #         if num != 0:
    #             sections[x//3 + (y//3)*3].append(num)
    #         else:
    #             mutable.append(y, x)
    # possible.append(search(puzzle))
    while possible:
        count += 1
        print(count)
        # print(possible)
        index = possible.pop()
        y, x = mutable[index]

        while success == False and puzzle[y][x] < 9:
            puzzle[y][x] += 1
            success = valid(puzzle[y][x], puzzle, fixed_sections[x//3 + (y//3)*3] + mutable_sections[x//3 + (y//3)*3])
        if success:
            y, x, poss = possible[-1]
            if puzzle[y][x] != poss and puzzle[y][x] != 0:  # removing from sections
                fixed_sections[x//3 + (y//3)*3].pop()
            puzzle[y][x] = poss
            fixed_sections[x//3 + (y//3)*3].append(poss)
            search_stuff = search(puzzle)
            if search_stuff == None:
                return puzzle
            possible.append(search_stuff)
        else:
            y, x, poss = possible.pop()
            if puzzle[y][x] == fixed_sections[x//3 + (y//3)*3][-1]:
                fixed_sections[x//3 + (y//3)*3].pop()
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
