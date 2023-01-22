from time import perf_counter


def remove_zero(alist):
    return [x for x in alist if x != 0]


def valid(y, x, puzzle, section, row, column):
    start = perf_counter()
    value = puzzle[y][x]
    return value not in row and value not in column and value not in section, (perf_counter() - start) * 1000


def begin(puzzle):
    start = perf_counter()
    mutable = []
    sections, rows, columns = [{k: set() for k in range(9)} for _ in range(3)]
    if len(puzzle) != 9:
        return False
    for y, line in enumerate(puzzle):
        if len(puzzle) != 9:
            return False
        for x, num in enumerate(line):
            if num > 9 or num < 0 or (num != 0 and not valid(y, x, puzzle, {}, {}, {})[0]):
                raise Exception
            else:
                if num == 0:
                    mutable.append((y, x))
                else:
                    rows[y].add(num)
                    columns[x].add(num)
                    sections[x//3 + (y//3)*3].add(num)
    print("begin time", (perf_counter() - start) * 1000)
    return mutable, sections, rows, columns


def solve_single(puzzle, seen=None):
    print(puzzle)
    # TODO improve speed by making a row and column sections list (like with sections)
    if seen == None:
        seen = set()
    mutable, sections, rows, columns = begin(puzzle)
    print(mutable)
    count = 0
    success = False
    index = 0
    seen = set()
    time = 0
    while True:
        count += 1
        y, x = mutable[index]
        sections_index = x//3 + (y//3)*3
        success = False
        square = puzzle[y][x]
        if square == 0:
            new = True
        else:
            sections[sections_index].remove(square)
            # print(y, x, square)
            rows[y].remove(square)
            columns[x].remove(square)

        while success == False and puzzle[y][x] < 9:
            puzzle[y][x] += 1
            success, add_to_time = valid(
                y, x, puzzle, sections[sections_index], rows[y], columns[x])
            time += add_to_time
        if success:
            # sections = add_to(sections, sections_index, puzzle[y][x])
            square = puzzle[y][x]
            sections[sections_index].add(square)
            rows[y].add(square)
            columns[x].add(square)
            index += 1
            if index == len(mutable):
                print("valid time", time)
                return puzzle
        else:
            index -= 1
            if index < 0:
                break
            puzzle[y][x] = 0
    print(count, "count")
    return "FAIL"


def sudoku_solver(puzzle):
    mutable, sections = begin(puzzle)


if __name__ == "__main__":
    start = perf_counter()
    print(solve_single([[0, 0, 0, 0, 0, 2, 7, 5, 0],
                        [0, 1, 8, 0, 9, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [4, 9, 0, 0, 0, 0, 0, 0, 0],
                        [0, 3, 0, 0, 0, 0, 0, 0, 8],
                        [0, 0, 0, 7, 0, 0, 2, 0, 0],
                        [0, 0, 0, 0, 3, 0, 0, 0, 9],
                        [7, 0, 0, 0, 0, 0, 0, 0, 0],
                        [5, 0, 0, 0, 0, 0, 0, 8, 0]]))
    print(f"{(perf_counter() - start) * 1000}")
