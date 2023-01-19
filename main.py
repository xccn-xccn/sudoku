from time import perf_counter

def search(puzzle):
    for y, line in enumerate(puzzle):
        for x, num in enumerate(line):
            if num == 0:
                return [y, x, 0]


def remove_zero(alist):
    return [x for x in alist if x != 0]


def valid(y, x, puzzle, section): #takes around 0.02 ms
    a = perf_counter()
    time = 0
    value = puzzle[y][x]
    line, column = remove_zero(puzzle[y]), remove_zero([line[x] for line in puzzle])
    if len(line) == len(set(line)) and len(column) == len(set(column)) and value not in section:
        return True, (perf_counter() - a)
    return False, (perf_counter() - a)


def begin(puzzle):
    mutable = []
    sections = [[] for _ in range(9)]
    rows, columns = {k: [] for k in range(9)} #work on this 
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
    # TODO improve speed by making a row and column sections list (like with sections)
    if seen == None:
        seen = set()
    mutable, sections = begin(puzzle)
    count = 0
    success = False
    index = 0
    multiple_solutions = False
    seen = set()
    while True:
        count += 1
        y, x = mutable[index]
        sections_index = x//3 + (y//3)*3
        success = False
        if puzzle[y][x] == 0:
            new = True
        else:
            sections[sections_index].pop()

        while success == False and puzzle[y][x] < 9:
            puzzle[y][x] += 1
            success, add_to_time = valid(y, x, puzzle, sections[sections_index])
            time += add_to_time

        if success:
            sections[sections_index].append(puzzle[y][x])
            index += 1
            if index == len(mutable):
                print(f"{time*1000} time ")
                return puzzle
        else:
            index -= 1
            if index < 0:
                break
            if not new:
                sections[sections_index].pop()
            puzzle[y][x] = 0
    print(count, "count")
    return "FAIL"


def sudoku_solver(puzzle):
    mutable, sections = begin(puzzle)


if __name__ == "__main__":
    start = perf_counter()
    print(solve_single([[8, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 3, 6, 0, 0, 0, 0, 0], [0, 7, 0, 0, 9, 0, 2, 0, 0], [0, 5, 0, 0, 0, 7, 0, 0, 0], [0, 0, 0, 0, 4, 5, 7, 0, 0], [0, 0, 0, 1, 0, 0, 0, 3, 0], [0, 0, 1, 0, 0, 0, 0, 6, 8], [0, 0, 8, 5, 0, 0, 0, 1, 0], [0, 9, 0, 0, 0, 0, 4, 0, 0]]))
    print(f"{(perf_counter() - start) * 1000}")