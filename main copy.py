def sudoku_solver(puzzle):
    print(puzzle)
    # TODO make it error on multiple solutions and refactor code is too slow on 17 hint puzzles

    def search():
        for y, line in enumerate(puzzle):
            for x, num in enumerate(line):
                if num == 0:
                    return [y, x, 0]

    def valid(details):
        y, x, attempt = details
        return True if attempt not in puzzle[y] and attempt not in [line[x] for line in puzzle] and attempt not in sections[x//3 + (y//3)*3] else False

    def able(puzzle):
        if len(puzzle) != 9:
            return False
        for line in puzzle:
            if len(puzzle) != 9:
                return False
            for num in line:
                if num > 9 or num < 0:
                    return False
        return True

    if not able(puzzle):
        raise Exception
    count = 0
    success = False
    sections = [[] for x in range(9)]
    possible = []
    for y, line in enumerate(puzzle):  # gets the numbers in the 3x3 area
        for x, num in enumerate(line):
            if num != 0:
                sections[x//3 + (y//3)*3].append(num)
    possible.append(search())
    while possible:
        count += 1
        print(count)
        # print(possible)
        while success == False and possible[-1][2] < 9:
            y, x, poss = possible[-1]
            possible[-1][2] += 1
            success = valid(possible[-1])
        if success:
            y, x, poss = possible[-1]
            if puzzle[y][x] != poss and puzzle[y][x] != 0:
                sections[x//3 + (y//3)*3].pop()
            puzzle[y][x] = poss
            sections[x//3 + (y//3)*3].append(poss)
            search_stuff = search()
            if search_stuff == None:
                return puzzle
            possible.append(search_stuff)
        else:
            y, x, poss = possible.pop()
            if puzzle[y][x] == sections[x//3 + (y//3)*3][-1]:
                sections[x//3 + (y//3)*3].pop()
            puzzle[y][x] = 0
        success = False
    raise Exception


if __name__ == "__main__":
    print(sudoku_solver([
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 0, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 1, 1, 2, 3, 4, 5, 6],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [9, 1, 2, 3, 4, 5, 6, 7, 8]]))
