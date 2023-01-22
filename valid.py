def valid(puzzle):  # sdlfs
    if len(puzzle) != 9:
        return False
    for line in puzzle:
        if len(puzzle) != 9:
            return False
        for num in line:
            if num > 9 or num < 0:
                return False
    return True


if __name__ == "__main__":
    print(valid([[0, 0, 0, 8, 0, 1, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 4, 3],
 [5, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 7, 0, 8, 0, 0],
 [0, 0, 0, 0, 0, 0, 1, 0, 0],
 [0, 2, 0, 0, 3, 0, 0, 0, 0],
 [6, 0, 0, 0, 0, 0, 0, 7, 5],
 [0, 0, 3, 4, 0, 0, 0, 0, 0],
 [0, 0, 0, 2, 0, 0, 6, 0, 0]]))
