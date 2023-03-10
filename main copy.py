from time import perf_counter


def search(puzzle):
    for y, line in enumerate(puzzle):
        for x, num in enumerate(line):
            if num == 0:
                return [y, x, 0]

def add_to_dict(dictionary, index, value):
    dictionary[index][len(dictionary[index])] = value
    return dictionary


def put_in(rows, columns, sections, y, x, value):
    rows = add_to_dict(rows, y, value)
    columns = add_to_dict(rows, x, value)
    sections = add_to_dict(rows, x//3 + (y//3)*3, value)
    return rows, columns, sections


def remove_zero(alist):
    return [x for x in alist if x != 0]


def valid(y, x, puzzle, section):  # takes around 0.02 ms
    value = puzzle[y][x]
    line, column = remove_zero(puzzle[y]), remove_zero([line[x] for line in puzzle])
    return len(line) == len(set(line)) and len(column) == len(set(column)) and value not in section.values()


def begin(puzzle):
    mutable = []
    sections, rows, columns = [{k: {} for k in range(9)} for _ in range(3)]
    if len(puzzle) != 9:
        return False
    for y, line in enumerate(puzzle):
        if len(puzzle) != 9:
            return False
        for x, num in enumerate(line):
            if num > 9 or num < 0 or (num != 0 and not valid(y, x, puzzle, {})):
                raise Exception
            else:
                if num == 0:
                    mutable.append((y, x))
                else:
                    rows, columns, sections = put_in(rows, columns, sections, y, x, num)
    return mutable, sections, rows, columns


def solve_single(puzzle, seen=None):
    print(puzzle)
    # TODO improve speed by making a row and column sections list (like with sections)
    if seen == None:
        seen = set()
    mutable, sections, a, b = begin(puzzle)
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
            sections[sections_index].popitem()

        while success == False and puzzle[y][x] < 9:
            puzzle[y][x] += 1
            success = valid(y, x, puzzle, sections[sections_index])

        if success:
            sections = add_to_dict(sections, sections_index, puzzle[y][x])
            # sections[sections_index].add(puzzle[y][x])
            index += 1
            if index == len(mutable):
                return puzzle
        else:
            index -= 1
            if index < 0:
                break
            if not new:
                sections[sections_index].popitem()
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
